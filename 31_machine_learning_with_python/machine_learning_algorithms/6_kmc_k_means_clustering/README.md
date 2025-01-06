K Means Clustering
---

- Allow us to cluster unlabeled data using unsupervised machine learning algorithm
- The overall goal is to divide data into distinct groups such that observations within each group are similar.
- How does this algorithm work?
    - Choose a number of clusters "K"
    - Randomly assign each point to a cluster
    - Until clusters stop changing, repeat the following:
        - For each cluster, compute cluster centroid by taking the mean vector of points in the cluster
        - Assign each data point to the cluster for which the centroid is the closest
- Choosing "K" value
    - Eblow method
        - Compute the sum of squared error (SSE) for some value of K (for eg: 2 4 6 8 etc)
        - SSE is defined as the sum of the squared distance between each member of the cluster and its centroid.
