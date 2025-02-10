import cv2
from cv2 import *
import face_recognition as fr
import os


# CREAR BASE DE DATOS
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for i in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{i}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(i)[0])


# CODIFICAR IMAGENES
def codificar(imagenes):

    # CREAR UNA LISTA NUEVA
    lista_codificada = []

    # PASAR TODAS LAS IMAGENES EN RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # CODIFICAR
        codificado = fr.face_encodings(imagen)[0]


        # AGREAR A LA LISTA DE CODIFICADOS
        lista_codificada.append(codificado)

    return lista_codificada


lista_empleados_codificada = codificar(mis_imagenes)

# TOMAR UNA IMAGEN DE LA CAMARA WEB
                         # (id, )
captura = cv2.VideoCapture(0, cv2.CAP_V4L)

# DSHOW (and MSMF) are windows only.
# on linux, use V4L, FFMPEG or GSTREAMER
# also, please check the return val of capture.set(), not all properties/values will be supported on any given machine


# LEER IMAGEN DE LA CAMARA
exito, imagen = captura.read()
print(captura.read()) # (False, None)


if not exito:
    print("No se ha podido tomar la imagen")
else:
    # RECONOCER CARA EN CAPTURA
    cara_captura = fr.face_locations(imagen)

    # CODIFICAR CARA EN CAPTURA
    cara_captura_codificada = fr.face_encodings(cara_captura)[0]

    # BUSCAR COINCIDENCIAS
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(caracodif, caraubic)
        distancias = fr.face_distance(caracodif, caraubic) # 5 distancias

        print(distancias)
