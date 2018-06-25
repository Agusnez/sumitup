from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X = np.array([[1,2,0], [1,4,0],[1,0,0],
            [4,2,0],[4,4,0],[4,0,0]])

kmeans = KMeans(n_clusters=2).fit(X)

print(kmeans.cluster_centers_)
for v in kmeans.cluster_centers_:
        print(v)

# Visualizacion
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X[:,0],X[:,1],X[:,2],c=kmeans.labels_)
ax.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],marker='+',s=200)
plt.show()