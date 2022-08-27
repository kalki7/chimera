# K-means
K-means is one of the simplest unsupervised clustering algorithms. The keywords/phrases are all vectorized into word embeddings, and then the vectors are placed onto an imaginary two-dimensional plane. 

The predefined K refers to the number of centroids (clusters) are placed and constantly shifted to draw clusters around the centroids, optimizing to reduce the distance between the centroid and the vectors for each of the K clusters. The centroids are allocated all the vectors closest to it, while keeping the clusters as small as possible.

The major issue with this is to define an optimal value for K (number of clusters) as we have no way of analyzing all groups possible in this unsupervised approach with unseen samples. To overcome this issue, we can use the [[Elbow Method for K-means]] to determine an optimal value for K.