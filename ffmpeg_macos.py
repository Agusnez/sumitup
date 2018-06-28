import subprocess
import os

def extraer_frames(ruta_video,ruta_destino,salto):
    subprocess.run(['mkdir',ruta_destino])
    subprocess.run(['./ffmpeg/bin/ffmpeg', '-i', ruta_video,'-r', str(salto)+'/1' ,ruta_destino + '/%03d.png'])

def mover_keyframes(ruta_fotogramas,lista_keyframes,ruta_destino):
    subprocess.run(['mkdir',ruta_destino])
    comando = ['cp']
    for cluster,valor in lista_keyframes.items():
        f = str(valor[1] + 1 )
        while(len(f)!=3):
            f = '0' + f
        comando.append(ruta_fotogramas + '/' + f + '.png')
    comando.append(ruta_destino)
    subprocess.run(comando)