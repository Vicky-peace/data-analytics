import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# generate blobs
dataset = make_blobs(n_samples=200, centers=4,n_features=2, cluster_std=1.6, random_state=50)

# convert to Arrays
points = dataset[0]

# create k means objects
kmeans = KMeans (n_clusters=4)

# fit the data object
kmeans.fit(points)

# plt points in scatterplot 
plt.scatter(dataset[0][:,0], dataset[0][:,1])

#get cluster centroids
clusters =kmeans.cluster_centers_

# Print the cluster centroids 
print(clusters)

# Get clusters
y_km = kmeans.fit_predict(points)

# color the points in each cluster
plt.scatter(points[y_km == 0,0], points[y_km == 0,1], s=50,color='red')
plt.scatter(points[y_km == 1,0], points[y_km == 1,1], s=50,color='green')
plt.scatter(points[y_km == 2,0], points[y_km == 2,1], s=50,color='yellow')
plt.scatter(points[y_km == 3,0], points[y_km == 3,1], s=50,color='cyan')

# display the centroids
plt.scatter(clusters[0][0], clusters [0][1],marker ='*', s=200,color='black')
plt.scatter(clusters[1][0], clusters [1][1],marker ='*', s=200,color='black')
plt.scatter(clusters[2][0], clusters [2][1],marker ='*', s=200,color='black')
plt.scatter(clusters[3][0], clusters [3][1],marker ='*', s=200,color='black')

# add legend
plt.legend()

# display the plot
plt.show()