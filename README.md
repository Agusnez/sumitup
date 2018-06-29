# Sum it up
Resumen automático de vídeos mediante clasificación. Trabajo para la asignatura Inteligencia Artificial.

# Estructura del código
El código se estructura en 2 ficheros auxiliares `cluster.py`,`ffmpeg.py` y uno principal `main.py`. Podrá observar que hay scripts para versiones de Windows y macOS, esto es porque las rutas y comandos para la creación de directorios son distintos en estos sistemas operativos.

### `cluster.py`
Este script contiene los métodos necesarios para analizar los fotogramas. Por una parte lee los fotogramas y los vectoriza según su histograma RGB y por otra aplica el algoritmo K-Medias y calcula qué fotograma está más cerca del centroide en cada clúster.

### `ffmpeg.py`
Automatiza las tareas que tienen que ver con la herramienta FFMPEG. Extrae los fotogramas de un vídeo, copia fotogramas de una carpeta a otra, etc. La versión Windows contiene más métodos útiles que la versión de macOS que sólo se enfoca al mínimo requerido en el trabajo.

### `main.py`
Es el script principal donde se ejecutan cada uno de los métodos de los ficheros auxiliares. Es el que usaremos para hacer los experimentos.

# Ejemplos de uso
A continuación se detalla cómo usar el script y los parámetros que se pueden configurar en el script principal.

