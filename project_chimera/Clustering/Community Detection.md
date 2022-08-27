# Community Detection
Community Detection is one of the most important tasks in network analysis where it helps partition the entire network into various communities for various tasks.

This has been algorithm has been modified to consider each one of the keyword/phrase embedding as a unique node and we partition them into clusters. Similar to the K-means algorithm, but instead of defining K (number of clusters), we will define some basic features of each community such as minimum items in the community, confidence threshold, etc. 

Unlike K-means, if the vector space has outliers, they aren't categorized into clusters, rather left out of the communities.