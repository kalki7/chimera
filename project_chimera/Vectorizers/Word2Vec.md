# Word2Vec
Word2Vec is a neural network approach that converts text by vectorizing individual words. The vectorized format of individual words in the vocabulary are known as word embeddings. Each word has a unique word embedding. These word embeddings are consolidated using various methods to vectorize the whole text document. One such method to obtain the word embeddings is Word2Vec.

There are a few architecures that help us achieve this vectorization
- [Continious Bag of Words (CBOW)](https://paperswithcode.com/method/cbow-word2vec)
- [Skip-gram](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)

These embeddings can be visualised through [Principal Component Analysis (PCA)](https://machinelearningmastery.com/principal-components-analysis-for-dimensionality-reduction-in-python/#:~:text=for%20Dimensionality%20Reduction-,Dimensionality%20Reduction%20and%20PCA,to%20predict%20the%20target%20variable.)