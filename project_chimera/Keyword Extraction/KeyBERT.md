# KeyBERT
With the use of BERT embeddings output from the respective vectorizer, we use then calculate the [max sum distance](https://maartengr.github.io/KeyBERT/api/maxsum.html) to extract the keywords.

The limit of the candidate list would be two times the number of keywords/phrases expected. The top-n combinations are then taken from the candidate list and combinations that are least similar by cosine similarity to each other are chosen. This proves effective when we have a small expected list of keywords due to it's exploding time complexity for large candidate lists.