from sklearn.cluster import KMeans
import numpy as np
import cv2
import os

carpeta = 'ffmpeg/bin/frames'

dataset = []

for imagen in os.listdir(carpeta):
    ruta = os.path.join(carpeta,imagen)
    #print(ruta)
    img = cv2.imread(ruta)

    color = ('b','g','r')
    histograma = []
    for i,col in enumerate(color):
        hist = cv2.calcHist([img],[i],None,[50],[0,256])
        for v in hist:
            histograma.append(v[0])
        
    dataset.append(histograma)

kmeans = KMeans(n_clusters=16).fit(dataset)
#print(kmeans.labels_)

clusters = {}

for i,c in enumerate(kmeans.labels_):
    if c not in clusters:
        clusters[c] = [i]
    else:
        clusters[c].append(i)
my_list = [elem[0] for elem in clusters.values()]
print(my_list)
