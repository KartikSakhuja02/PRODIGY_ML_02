import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

data = pd.read_csv("Mall_Customers.csv")
features = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
data = data[features].dropna()

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

kmeans = KMeans(n_clusters=5, init='random', max_iter=1, random_state=42, n_init=1)

for iteration in range(5):
    kmeans.max_iter = iteration + 1
    kmeans.fit(data_scaled)
    
    pca = PCA(n_components=2)
    data_pca = pca.fit_transform(data_scaled)
    
    plt.scatter(data_pca[:, 0], data_pca[:, 1], c=kmeans.labels_, cmap='viridis', marker='o')
    plt.title(f"Iteration {iteration + 1}")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.colorbar()
    plt.show()

print(kmeans.cluster_centers_)
print(pd.Series(kmeans.labels_).value_counts())
