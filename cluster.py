from sklearn.cluster import KMeans
import numpy as np
import cv2
import os

def lee_frames(carpeta, h, t):

    tam_histograma = h
    dataset = []
    cont = t   

    for imagen in os.listdir(carpeta):
        if cont%t==0:

            ruta = os.path.join(carpeta,imagen)
            img = cv2.imread(ruta)
            
            color = ('b','g','r')
            histograma = []
            for i,col in enumerate(color):
                hist = cv2.calcHist([img],[i],None,[tam_histograma],[0,256])
                for v in hist:
                    histograma.append(v[0])
                
            dataset.append(histograma)

        cont = cont + 1        

    return dataset

def clusterizar(dataset,k):
    kmeans = KMeans(n_clusters=k).fit(dataset)
    matriz_distancias = kmeans.transform(dataset)

    minimos = {}
    for i,p in enumerate(kmeans.labels_):
        distancia = matriz_distancias[i][p]
        if p not in minimos or minimos[p][0] > distancia:
            minimos[p] = [distancia, i]
    
    return minimos