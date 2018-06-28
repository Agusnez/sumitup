import subprocess
import sys
import os

def obtain_frames(ruta_carpeta_video,v_origen,n_frame_outx1_frame_in):

    carpeta_destino = v_origen + '_fotogramas'
    subprocess.Popen('cd ' + ruta_carpeta_video + ' && md ' + carpeta_destino, shell=True, stdout=subprocess.PIPE).stdout.read()

    if n_frame_outx1_frame_in != 1:
        a = str(n_frame_outx1_frame_in)
        comando_r = 'ffmpeg -i '+ v_origen + ' -r ' + a + '/1 ' + carpeta_destino + '/%03d.png'
        subprocess.Popen('cd ' + ruta_carpeta_video + ' && ' + comando_r, shell=True, stdout=subprocess.PIPE).stdout.read()
        print('Extraido 1 de cada ' + a + ' fotogramas del video ' + v_origen + ' y guardados en la carpeta '+ carpeta_destino)
    else:
        comando = 'ffmpeg -i '+ v_origen + ' ' + carpeta_destino + '/%03d.png'
        subprocess.Popen('cd ' + ruta_carpeta_video + ' && ' + comando, shell=True, stdout=subprocess.PIPE).stdout.read()
        print('Extraidos todos los fotogramas del video ' + v_origen + ' en la carpeta '+ carpeta_destino)

#obtain_frames('C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin','40_seg_video.mp4',5)


def mover_fotogramas(ListaKeyFrames,ruta_carpeta_origen,ruta_carpeta_destino):

    n = str(len(ListaKeyFrames))
    for i in ListaKeyFrames:
        subprocess.Popen('copy ' + ruta_carpeta_origen + '\\' + i + '.png ' + ruta_carpeta_destino + '\\' + i + '.png', shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf8").strip()
    print('Se han copiado un total de ' + n + ' fotogramas')

#list2= ['002','019','047','060']
#mover_fotogramas(list2,'C:\\Users\\franc\\ETSII\\INPUTPATH','C:\\Users\\franc\\ETSII\\OUTPUTPATH')


def video_fps(ruta_carpeta_video,nombre_video):

    ruta_cmd = 'cd ' + ruta_carpeta_video
    v_fps = subprocess.Popen(ruta_cmd + ' && ffprobe -v 0 -of csv=p=0 -select_streams v:0 -show_entries stream=r_frame_rate '+ nombre_video, shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf8")
    a,b = (int(x) for x in v_fps.split('/'))
    fps= a/b
    trun_fps=round(fps,2)
    print('El video '+ nombre_video + ' se reproduce a', str(trun_fps) , 'fps')
    return trun_fps

#video_fps('C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin','40_seg_video.mp4')


def seg_desde_frame(ruta_carpeta_origen,nombre_carpeta_dst,nombre_video,frame,seg):

    fps = video_fps(ruta_carpeta_origen,nombre_video)
    frame_int = int(frame)
    seg_inicial = int(frame_int/fps)
    seg_final = seg_inicial+seg
    frames_seccion = int(seg*fps)

    print(fps,seg_inicial,seg_final,frames_seccion)

    comando = 'ffmpeg -i '+ nombre_video + ' -ss 00:00:' + str(seg_inicial) + ' -frames:v ' + str(frames_seccion) + ' -start_number ' + frame + ' ' + nombre_carpeta_dst + '/' + '%03d.png'
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

def rename_frames(ruta_carpeta_origen):
    cont = 1
    for filename in os.listdir(ruta_carpeta_origen):
        os.rename(os.path.join(ruta_carpeta_origen,filename), 
                  os.path.join(ruta_carpeta_origen,str(cont)+'.png'))
        cont = cont + 1

#rename_frames('C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin\\40_seg_video.mp4_fotogramas_secciones')

def unir_frames(carpeta_fotogramas,nombre_archivo_dst):
    
    ruta_carpeta_ffmpeg = 'C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin'
    comando = 'cd ' + ruta_carpeta_ffmpeg + ' && ffmpeg -i ' + carpeta_fotogramas + '\%d.png -c:v libx264 -vf fps=24 -s 1280x720 ' + nombre_archivo_dst
    subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE).stdout.read()

unir_frames('C:\\Users\\franc\\ETSII\\40_seg_video.mp4_fotogramas_secciones','hecho.mp4')

#def video_to_frames(command):
#    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True, universal_newlines=False)
#    stdout = process.communicate()[0].decode("utf8").strip()
#    print(stdout)
#
#video_to_frames('cd C:\\Users\\franc\\ETSII\\Curso 2017-2018\\IA\\Trabajo\\ffmpeg-4.0-win64-static\\bin && md cap2 && ffmpeg -i 40_seg_video.mp4 -r 5/1 cap2/%03d.png')