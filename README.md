Task 02 - Create a K-means clustering algorithm to group customers of a retail store based on their purchase history.
Given Dataset: Customer Segmentation Data

K-means clustering algorithm: It’s an unsupervised machine learning approach where we aren’t trying to predict an outcome, but rather discover patterns in the dataset. The idea here is to find clusters in the data, meaning groups of data points that share some similarities. Unlike traditional machine learning algorithms, K-means doesn’t work on labeled data but instead learns the structure of the dataset through iterative steps.

Cluster:
Clusters are essentially blocks of data that share common properties. The goal of K-means is to assign each data point to one of these clusters.

Steps involved in building the K-means algorithm:
1. Dataset: First, obtain a dataset, which is often in .csv format.

2. Specify K (number of clusters): Define how many clusters you want to segment the data into. This number (K) is usually determined before running the algorithm.

3. Randomly initialize centroids: Centroids are points representing the center of each cluster. Initially, they are chosen randomly from the dataset.

4. Assign data points to clusters: Each data point is assigned to the cluster whose centroid is closest to it. This is done by calculating the distance between the data point and the centroid.

5. Update centroids: Once all points are assigned, the centroid of each cluster is recalculated based on the geometric mean of all the points in that cluster.

6. Iterations: The algorithm runs iteratively, updating the centroids and reassigning points until the centroids no longer change (or change very little), indicating that the clustering is complete.

The task02.py code works in the following steps

1. I first define the number of clusters (K) and initialize centroids randomly.
2. Then I assign the data points to the clusters based on their proximity to the centroids.
3. The centroids are updated in each iteration, and the algorithm runs until it converges.
4. By running these iterations, the code generates the final clusters, which group the customers based on similarities in their purchase history (like Age, Annual Income, and Spending Score).
