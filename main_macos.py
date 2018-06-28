from cluster import *
from ffmpeg_macos import mover_keyframes
import argparse

parser = argparse.ArgumentParser(description='Encuentra los fotogramas clave dada una lista de fotogramas.')
parser.add_argument('ruta', type=str, help='Ruta donde se encuentra la lista de fotogramas.')
parser.add_argument('--k', dest='n_clusters', type=int, default=8, help='Número de clusters.')
parser.add_argument('--t', dest='salto', type=int, default=1, help='Salto de fotogramas en la lista de fotogramas.')
parser.add_argument('--h', dest='tam_histograma', type=int, default=50, help='Tamaño del histograma.')
parser.add_argument('--out', dest='ruta_destino', type=str, default='OUTPUTPATH', help='Ruta donde irán los fotogramas clave.')
args = parser.parse_args()

print('Ejecutando el programa con ' + str(args.n_clusters) + ' clusters')
print('Leyendo un fotograma por cada ' + str(args.salto) + ' fotograma(s).')
print('Tamaño del histograma = ' + str(args.tam_histograma))

dataset = lee_frames(args.ruta,args.tam_histograma,args.salto)
fotogramas_clave = clusterizar(dataset,args.n_clusters)
mover_keyframes(args.ruta,fotogramas_clave,args.ruta_destino)

