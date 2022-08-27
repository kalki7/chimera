import re

from treelib import Tree

import numpy as np
import pandas as pd

from keybert import KeyBERT
from sentence_transformers import SentenceTransformer, util
from keyphrase_vectorizers import KeyphraseCountVectorizer

class chimera():

    def __init__(self, domain=None, obj=None):
        
        if type(obj)!=list:
            obj = [obj]
        
        if type(obj[0])!=str:
            raise ValueError("Please pass str only, not {}.".format(type(obj[0])))
        
        if type(domain)!=str:
            raise ValueError("Please pass str only, not {}.".format(type(obj[0])))
        
        self.domain = domain
        
        self.data = []
        for i in obj:
            self.data.append(self.clean(i))
        
        self.cluster = []
        self.keys = []
        self.tree = Tree()

        self.keybert = KeyBERT()
        self.vectorizer = KeyphraseCountVectorizer()
        self.sentbert = SentenceTransformer('all-MiniLM-L6-v2')

    #clean text
    def clean(self, raw_text):

        text = re.sub(r"https?://\S+", "", raw_text)
        text = re.sub(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", "", text)
        text = text.replace("&amp;", " ")
        text = re.sub(r"<[.*?]+>", " ", text)
        text = re.sub(r"^\d$", " ", text)
        text = text.replace("\'\'","'")
        text = text.replace("\\"," ")

        return text

    #extract initial set of keywords from raw text
    def extract_keyword(self, text=None, min_df=5, lang="english", top_n=20):
        
        if text==None:
            text = self.clean(self.data[0])
        
        results = set()

        try:

            keywords = self.keybert.extract_keywords(text, vectorizer=self.vectorizer, top_n=top_n, min_df= min_df, stop_words=lang)
            for scored_keywords in keywords:
                for keyword in scored_keywords:
                    if isinstance(keyword, str):
                        results.add(keyword)
                        
            keywords = self.keybert.extract_keywords(text, keyphrase_ngram_range=(1, 3), top_n=top_n, min_df= min_df, stop_words=lang, use_maxsum=True,nr_candidates=top_n)
            for scored_keywords in keywords:
                for keyword in scored_keywords:
                    if isinstance(keyword, str):
                        results.add(keyword)
        
        except Exception:
            pass
                    
        return list(results)
    
    #extract communities and their respective names
    def community_detecter(self, domain_keys, cluster_accuracy=75, min_cluster_size=2,batch_size=256):
        
        cluster_col = "Cluster Name"
        key_col = "Keywords"
        len_col = "Length"

        df = pd.DataFrame(domain_keys).rename(columns={0:key_col})
        
        cluster_name_list = []
        corpus_sentences_list = []
        df_all = []

        corpus_set = set(df[key_col])
        corpus_set_all = corpus_set
        cluster = True

        cluster_accuracy = cluster_accuracy / 100

        while cluster:

            corpus_sentences = list(corpus_set)
            check_len = len(corpus_sentences)

            corpus_embeddings = self.sentbert.encode(corpus_sentences, batch_size=batch_size, show_progress_bar=False, convert_to_tensor=True)
            clusters = util.community_detection(corpus_embeddings, min_community_size=min_cluster_size, threshold=cluster_accuracy)

            for keyword, cluster in enumerate(clusters):
                for sentence_id in cluster[0:]:
                    corpus_sentences_list.append(corpus_sentences[sentence_id])
                    cluster_name_list.append("Cluster {}, #{} Elements ".format(keyword + 1, len(cluster)))

            df_new = pd.DataFrame(None)
            df_new[cluster_col] = cluster_name_list
            df_new[key_col] = corpus_sentences_list

            df_all.append(df_new)
            have = set(df_new[key_col])

            corpus_set = corpus_set_all - have
            remaining = len(corpus_set)
            if check_len==remaining:
                break

        df_new = pd.concat(df_all)
        df = df.merge(df_new.drop_duplicates(key_col), how='left', on=key_col)

        df[len_col] = df[key_col].astype(str).map(len)
        df = df.sort_values(by=len_col, ascending=True)

        df[cluster_col] = df.groupby(cluster_col)[key_col].transform('first')
        df.sort_values([cluster_col, key_col], ascending=[True, True], inplace=True)

        del df[len_col]

        col = df.pop(key_col)
        df.insert(0, col.name, col)

        col = df.pop(cluster_col)
        df.insert(0, col.name, col)

        df.sort_values([cluster_col, key_col], ascending=[True, True], inplace=True)

        # uncluster_percent = (remaining / len(domain_keys)) * 100
        # clustered_percent = 100 - uncluster_percent


        return df[cluster_col].to_list(), df[key_col].to_list() 
    
    #run to extract a two level knowledge tree
    def pipeline(self, noise=False):
        
        self.cluster = []
        self.keys = []
        
        domain_key = []

        for i in range(len(self.data)):
            self.keys.append(self.extract_keyword(self.data[i]))
            domain_key += self.keys[i]
            
        domain_keys = list(set(domain_key))
        
        lv1, og = self.community_detecter(domain_keys)
        
        lv2, lv1_2 = self.community_detecter(lv1)
        
        for i in range(len(og)):
            
            l2 = lv2[lv1_2.index(lv1[i])]
            if l2 is np.nan:
                l2 = lv1[i]
                if l2 is np.nan:
                    l2 = og[i]
                    l1 = np.nan
                    l0 = np.nan
                else: 
                    l1 = og[i]
                    l0 = np.nan
            else:
                l1 = lv1[i]
                l0 = og[i]
            
            item_data = {
                "2":l2,
                "1":l1,
                "0":l0
            }
    
            self.cluster.append(item_data)
        
        df = pd.DataFrame(self.cluster)
        
        if noise==False:
            df = df.dropna(thresh=df.shape[1]-1, axis=0)
        
        return(df)
    
    def add_tree(self,i,j):

        try:
            if j==2 and i[str(j-1)] is not np.nan:
                if i[str(j)]!=self.domain:
                    self.tree.create_node(i[str(j)],i[str(j)],parent=self.domain)
            else:
                if i[str(j)]!=i[str(j+1)] and len(i[str(j)].split(' '))>len(i[str(j+1)].split(' ')):
                    self.tree.create_node(i[str(j)],i[str(j)],parent=i[str(j+1)])

        except Exception:
            pass


    def visualize(self):
        
        self.tree = Tree()
        
        self.tree.create_node(self.domain,self.domain)
        
        for i in self.cluster:
            for j in [2,1,0]:
                if i[str(j)] is not np.nan:
                    self.add_tree(i,j)
                    
        self.tree.show()