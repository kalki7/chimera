# Keyword Extraction
Given a document and a list of extracted candidate keywords/phrases, the top n keywords are extracted based on the context of the document. The candidate list is extracted from the [[POS Tagger]] and the context of the document is derived through the [[Vectorizers]].

The methods we're looking into are the
- [[Document keyphrase matrix]]
- [[KeyBERT]]

A few ranking algorithms that we consider include
- [TextRank](https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf)
- [SingleRank](https://aclanthology.org/C08-1122.pdf)
- [EmbedRank](https://aclanthology.org/K18-1022.pdf)

> Note that we don't use any of these ranking algorithms, rather have look for a group of least similar keywords/phrases
