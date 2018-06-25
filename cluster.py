from sklearn.cluster import KMeans
import numpy as np
import cv2
import os

carpeta = 'frutas'

dataset = []

for imagen in os.listdir(carpeta):
    ruta = os.path.join(carpeta,imagen)
    print(ruta)
    img = cv2.imread(ruta)

    color = ('b','g','r')
    histograma = []
    for i,col in enumerate(color):
        hist = cv2.calcHist([img],[i],None,[3],[0,256])
        for v in hist:
            histograma.append(v[0])
        
    dataset.append(histograma)

kmeans = KMeans(n_clusters=2).fit(dataset)
print(kmeans.labels_)