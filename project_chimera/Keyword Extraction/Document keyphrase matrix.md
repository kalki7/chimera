# Document keyphrase matrix
It is a matrix representation of the frequencies of keywords/phrases that occur in a given set of documents. The rows represent the text while the columns indicate the unique keywords/phrases. 

This matrix can be generated with the Tfidf vecotrs or BOW (Count) Vectors. In this matrix, instead of taking the entire vocabulary, we take only those extracted and tagged candidates and pass that through a regex filter that helps extract phrases.

The top-n keywords are filtered by the least similar candidates using cosine similarity.

