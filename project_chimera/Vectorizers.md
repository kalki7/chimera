# Vectorizers
Vectorizers convert text into a numerical representation. This process is known as text vectorization.

A few popular vectorisers include:
- [[Bag of Words Vectorizer]]
- [[Tfidf Vectorizer]]
- [[Word2Vec]]
- [[BERT]]

Each vectorizer has it's own set of pros and cons with respect to how the contextual data of the language is preserved to computational restrictions.

### Pre-processing Data
Before we vectorize our data, we do not require words that add no meaning to the corpus of text as they might be redundant due to the lack of contextual value they add to the text and might also add noise due the massive frequency of its occurance during the converstion process. These words are commonly knows as stopwords.

With respect to normalisation of the words with techniques such as stemming or lemmatisation will not be necessary as in our approach, the minor delta in words will be key in understanding and creating the knowledge tree.