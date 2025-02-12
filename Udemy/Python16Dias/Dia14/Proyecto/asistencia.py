## REGISTRO CON CONOCIMIENTO FACIAL

import cv2
from cv2 import *
import face_recognition as fr # Se debe importar de esta manera, ya que 'face_recognition' es palabra reservada
import os
import numpy as np
from datetime import datetime


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

        # CODIFICAR - RECONOCER LOS ROSTROS
        codificado = fr.face_encodings(imagen)[0]

        # AGREAR A LA LISTA DE CODIFICADOS
        lista_codificada.append(codificado)

    return lista_codificada

# REGISTRAR LOS INGRESOS
def registrar_ingresos(persona):
    # Abrir y escribir ("r+")
    file = open('registro.csv', "r+")
    lista_datos = file.readlines()
    nombres_registro = []

    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])


    if persona not in nombres_registro:
        now = datetime.now()
        string_now = now.strftime("%d/%m/%Y %H:%M:%S")
        file.writelines(f"\n{persona}, {string_now}")



lista_empleados_codificada = codificar(mis_imagenes)


# TOMAR UNA IMAGEN DE LA CAMARA WEB
                         # (id, )
captura = cv2.VideoCapture(0, cv2.CAP_V4L)


# DSHOW (and MSMF) are windows only.
# on linux, use V4L, FFMPEG or GSTREAMER
# also, please check the return val of capture.set(), not all properties/values will be supported on any given machine


# LEER IMAGEN DE LA CAMARA
exito, imagen = captura.read()
# print(captura.read()) # (False, None) or (True)

# SI NO HAY EXITO AL TOMAR LA CAPTURA
if not exito:
    print("No se ha podido tomar la imagen")
else:

    # RECONOCER CARA EN CAPTURA
    cara_captura = fr.face_locations(imagen)
    print("LOCACION DE CARA ", cara_captura)

    try:
        # CODIFICAR CARA CAPTURADA
        cara_captura_codificada = fr.face_encodings(imagen, cara_captura)[0]
        # print("Codificacion de cara ", cara_captura_codificada)
    except IndexError:
        print("No se ha podido tomar la imagen")


    #BUSCAR COINCIDENCIAS EN BASE DE DATOS
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        # COINCIDENCIAS DE IMAGEN EN LA BASE DE DATOS
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        # DISTANCIA DE PARECIDO CON LOS EMPLEADOS EN BASE DE DATOS
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(f"Coincidencias: {coincidencias}\nDistancias: {distancias}")

        # DEVUELVE EL NUMERO MENOR EN LA LISTA DE DISTANCIAS
        inidice_coincidencia = np.argmin(distancias)

        # MOSTRAR COINCIDENCIAS SI LAS HAY
        if distancias[inidice_coincidencia] > 0.5:
            print("No coincide con ninguno de nuestros empleados")
        else:
            # BUSCAR NOMBRE DEL EMPLEADO ENCONTRADO
            nombre = nombres_empleados[inidice_coincidencia]

            # 4 Puntos de la cara encontrada
            y1, x2, y2, x1 = caraubic
            # DIBUJAMOS CUADRADO
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # MOSTRAR MENSAJE
            cv2.rectangle(imagen, (x1, y1 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 0), 2)

            registrar_ingresos(nombre)

            # MOSTRAR LA IMAGEN OBTENIDA
            cv2.imshow("Imagen Web", imagen)
            # MANTENER VENTANA ABIERTA
            cv2.waitKey(0)

            print(f"Bienvenido {lista_empleados[nombre]}")




