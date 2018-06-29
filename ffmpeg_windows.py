import subprocess
import sys
import os

ruta_ffmpeg = 'C:\\Users\\franc\\IA\\ffmpeg\\bin'

def extraer_frames(ruta_carpeta_video,nombre_video):

    carpeta_inputpath = ruta_carpeta_video + '\\' + nombre_video + '_INPUTPATH'
    carpeta_outputpath = ruta_carpeta_video + '\\' + nombre_video + '_OUTPUTPATH'
    subprocess.Popen('cd ' + ruta_carpeta_video + ' && md ' + carpeta_inputpath, shell=True, stdout=subprocess.PIPE).stdout.read()

    comando = 'ffmpeg -i '+ ruta_carpeta_video + '\\' + nombre_video + ' ' + carpeta_inputpath + '/%d.png'
    subprocess.Popen('cd ' + ruta_ffmpeg + ' && ' + comando, shell=True, stdout=subprocess.PIPE).stdout.read()
    print('Extraidos todos los fotogramas del video ' + nombre_video + ' en la carpeta INPUTPATH')

    return carpeta_inputpath,carpeta_outputpath

#extraer_frames('C:\\Users\\franc\\IA\\Videos','1_min_travel_video.mp4')

def obtain_frames(ruta_carpeta_video,nombre_video,framesxseg):

    carpeta_destino = nombre_video + '_fotogramas'
    subprocess.Popen('cd ' + ruta_carpeta_video + ' && md ' + carpeta_destino, shell=True, stdout=subprocess.PIPE).stdout.read()

    if framesxseg != 1: 
        comando_r = 'ffmpeg -i '+ nombre_video + ' -r ' + str(framesxseg) + '/1 ' + carpeta_destino + '/%d.png'
        subprocess.Popen('cd ' + ruta_carpeta_video + ' && ' + comando_r, shell=True, stdout=subprocess.PIPE).stdout.read()
        print('Extraidos ' + str(framesxseg) + ' fotogramas por segundo del video ' + nombre_video + ' y guardados en la carpeta '+ carpeta_destino)
    else:
        comando = 'ffmpeg -i '+ nombre_video + ' ' + carpeta_destino + '/%d.png'
        subprocess.Popen('cd ' + ruta_carpeta_video + ' && ' + comando, shell=True, stdout=subprocess.PIPE).stdout.read()
        print('Extraidos todos los fotogramas del video ' + nombre_video + ' en la carpeta '+ carpeta_destino)

#obtain_frames('C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin\\','1_min_travel_video.mp4',12)


def mover_fotogramas_clave(ruta_carpeta_origen,ListaKeyFrames,ruta_carpeta_destino):

    n = str(len(ListaKeyFrames))
    subprocess.Popen('md ' + ruta_carpeta_destino, shell=True, stdout=subprocess.PIPE).stdout.read()
    list_keyframes = []

    for cluster,valor in ListaKeyFrames.items():
        list_keyframes.append(valor[1])
        subprocess.Popen('copy ' + ruta_carpeta_origen + '\\' + str(valor[1]) + '.png ' + ruta_carpeta_destino + '\\' + str(valor[1]) + '.png', shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf8").strip()
    print('Se han copiado un total de ' + n + ' fotogramas a ' + ruta_carpeta_destino)

    return list_keyframes

#dict2= {1: [0.0, 0], 2: [84348.88298724829, 430], 6: [68962.82333700213, 562], 5: [56149.5328624734, 941], 4: [8888.559053760348, 98], 3: [39396.81050140705, 631], 0: [91625.49265176337, 838], 7: [88456.82270587997, 815]}
#mover_fotogramas_clave('C:\\Users\\franc\\ETSII\\INPUTPATH',dict2,'C:\\Users\\franc\\ETSII\\OUTPUTPATH')


def video_fps(ruta_carpeta_video,nombre_video):

    ruta_cmd = 'cd ' + ruta_carpeta_video
    v_fps = subprocess.Popen(ruta_cmd + ' && ffprobe -v 0 -of csv=p=0 -select_streams v:0 -show_entries stream=r_frame_rate '+ nombre_video, shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf8")
    a,b = (int(x) for x in v_fps.split('/'))
    fps= a/b
    trun_fps=round(fps,2)
    print('El video '+ nombre_video + ' se reproduce a', str(trun_fps) , 'fps')
    return trun_fps

#video_fps('C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin','1_min_travel_video.mp4')


def seg_desde_frame(ruta_carpeta_origen,nombre_carpeta_dst,nombre_video,frame,seg):

    fps = video_fps(ruta_carpeta_origen,nombre_video)
    frame_int = int(frame)
    seg_inicial = int(frame_int/fps)
    seg_final = seg_inicial+seg
    frames_seccion = int(seg*fps)

    print(fps,seg_inicial,seg_final,frames_seccion)

    comando = 'ffmpeg -i '+ nombre_video + ' -ss 00:00:' + str(seg_inicial) + ' -frames:v ' + str(frames_seccion) + ' -start_number ' + frame + ' ' + nombre_carpeta_dst + '/' + '%d.png'
    subprocess.Popen('cd ' + ruta_carpeta_origen + ' && ' + comando, shell=True, stdout=subprocess.PIPE).stdout.read()
    print('Extraidos los fotogramas del video ' + nombre_video + ' desde el segundo ' + str(seg_inicial) + ' hasta el ' + str(seg_final) + ' y guardados en la carpeta '+ nombre_carpeta_dst)

#seg_desde_frame('C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin','cap_fotogramas','40_seg_video.mp4','200',4)


def secciones_desde_lista(ListaKeyFrames,ruta_carpeta_origen,nombre_video,seg_desde_frames):

    carpeta_destino = nombre_video + '_fotogramas_secciones'
    subprocess.Popen('cd ' + ruta_carpeta_origen + ' && md ' + carpeta_destino, shell=True, stdout=subprocess.PIPE).stdout.read()

    for i in ListaKeyFrames:
        seg_desde_frame(ruta_carpeta_origen,carpeta_destino,nombre_video,i,seg_desde_frames)

#list1= ['008','051','190','405','523']
#secciones_desde_lista(list1,'C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin','40_seg_video.mp4',3)

def rename_frames(ruta_carpeta_frames):
    cont = 1
    for filename in os.listdir(ruta_carpeta_frames):
        os.rename(os.path.join(ruta_carpeta_frames,filename), 
                  os.path.join(ruta_carpeta_frames,str(cont)+'.png'))
        cont = cont + 1

#rename_frames('C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin\\40_seg_video.mp4_fotogramas_secciones')

def unir_keyframes(carpeta_keyframes,carpeta_dst,nombre_video_original):
    
    comando = 'cd ' + ruta_ffmpeg + ' && ffmpeg -framerate 2/3 -i ' + carpeta_keyframes + '\%d.png -c:v libx264 -vf fps=23 -s 1280x720 resumen_' + nombre_video_original
    subprocess.Popen(comando + ' && move resumen_' + nombre_video_original + ' ' + carpeta_dst + '\\resumen_' + nombre_video_original, shell=True, stdout=subprocess.PIPE).stdout.read()

def unir_frames(carpeta_fotogramas,nombre_archivo_dst):
    
    comando = 'cd ' + ruta_ffmpeg + ' && ffmpeg -i ' + carpeta_fotogramas + '\%d.png -c:v libx264 -vf fps=24 -s 1280x720 ' + nombre_archivo_dst
    subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE).stdout.read()

#unir_frames('C:\\Users\\franc\\ETSII\\40_seg_video.mp4_fotogramas_secciones','hecho.mp4')

#def video_to_frames(command):
#    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True, universal_newlines=False)
#    stdout = process.communicate()[0].decode("utf8").strip()
#    print(stdout)
#
#video_to_frames('cd C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin && md cap2 && ffmpeg -i 40_seg_video.mp4 -r 5/1 cap2/%03d.png')