# Elbow Method for K-means
A fundamental issue in the [[K-means]] clustering algorithm is to dynamically find the value of K. The elbow method helps us determine an optimal value for K.

First we select the possible range for K. We then iterate the K-means clustering algorithm with each individual value in the given range for K while we also calculate the distortion and inertia for each clustering model.
- Distortion : average squared distance from the centroids and the clusters
- Intertia : sum of squared distances of samples of the closest centroid

We will then have to plot the disortion and inertia values against each value of K. Once we have this representation, we will have to select the value of K at the elbow point of the graph.

Although the optimal K is found, it is still calls for human intervention to identify the precise elbow point. This means that the system still calls for manual intervention.