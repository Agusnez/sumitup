from cluster import *
from ffmpeg_windows import *
import argparse

def main_win(ruta_carpeta_video,nombre_video,T,K,H):
    carpeta_input,carpeta_output = extraer_frames(ruta_carpeta_video,nombre_video)
    dataset = lee_frames(carpeta_input,H,T)
    fotogramas_clave = clusterizar(dataset,K)
    lista_keyframes = mover_fotogramas_clave(carpeta_input,fotogramas_clave,carpeta_output)
    rename_frames(carpeta_output)
    unir_keyframes(carpeta_output,ruta_carpeta_video,nombre_video)
    print('Ejecutando el programa con ' + str(K) + ' clusters')
    print('Leyendo un fotograma por cada ' + str(T) + ' fotograma(s).')
    print('Tamaño del histograma = ' + str(H))
    print('Carpeta INPUTPATH donde se encuentran los fotorgramas: ' + carpeta_input)
    print('Carpeta OUTPUTPATH donde se encuentran los keyframes: ' + carpeta_output)
    print('El video resumen ha sido creado a partir de la siguiente lista de frames originales: ' + str(lista_keyframes))


main_win('C:\\Users\\franc\\IA\\Videos','40_seg_video.mp4',1,8,50)


