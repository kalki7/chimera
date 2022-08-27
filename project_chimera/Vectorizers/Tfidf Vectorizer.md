# Tfidf Vectorizer
Term frequency-inverse document frequency converts text into vectors by multiplying the term frequency and inverse document frequency.

Given a set of documents, a set of unique words from all the documents knowns as the vocabulary is extracted.

Term frequency matrix consists of each of the text documents in the rows and the set of words from the vocabulary in the columns, populated by the count word occurances in each document.

Inverse document frequency matrix is similar to the the term frequency matrix, but is populated with the log of the total number of documents by the number of documents in which a word has occured.

The product of these two matrices gives us the Tfidf vector space.