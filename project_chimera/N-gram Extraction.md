# N-gram Extraction
Now that we have our respective keywords grouped into various communities from [[Clustering]], we need to extract a common N-gram word as a label for each community. For this we will extract the shortest N-gram keyword from the cluster.

This is done by a small custom written algorithm. 