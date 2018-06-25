# Script para probar que funciona correctamente OpenCV
# Muestra un histograma de una imagen
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('fotos/budapest.jpg')

hist = cv2.calcHist([img],[0],None,[256],[0,256])

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[50],[0,256])
    plt.plot(histr,color = col)
    #plt.xlim([0,15])
    print('Histograma B: ' + str(len(histr)))
    print(histr)
plt.show()


