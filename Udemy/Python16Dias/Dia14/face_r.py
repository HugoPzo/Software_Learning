import cv2
import face_recognition as fr

# CARGAR IMAGENES
foto_control = fr.load_image_file("fotoA1.jpeg")
foto_prueba = fr.load_image_file("brad_pitt.jpg")

# PASAR IMAGENES A RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)


# HALLAR CARAS DENTRO DE LAS FOTOS
# Localizar cara dentro de la foto
lugar_cara_A = fr.face_locations(foto_control)[0] # [(247, 932, 632, 546)]
lugar_cara_B = fr.face_locations(foto_prueba)[0]

# CODIFICAR LA CARA DETECTADA -> MANDAR DATOS QUE ENTIENDA LA COMPUTADORA
cara_codificada_A = fr.face_encodings(foto_control)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# MARCAR CARA EN LA FOTO - RECTANGULO

# FOTO
# Vertices x, y
# Vertices x, y - Opuesto
# Color Rectangulo
# Borde Cuadrado Tamaño
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]), 
              (lugar_cara_A[1], lugar_cara_A[2]), 
              (0, 255, 0), 
              2) 

cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (0, 255, 0),
              2) 

# REALIZAR COMPARACION - tolerance = Limite nivel de Similitud 
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B, tolerance=0.4)
print(resultado) # [np.False_] or [np.True_]


# MEDIDA DE LA DISTANCIA (SIMILITUD/COINCIDENCIA)
    # MENOR DISTANCIA - MAYOR COINCIDENCIA || MAYOR DISTANCIA - MENOR COINCIDENCIA
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
print(distancia) # Brad Pitt [0.75595785]


# MOSTRAR RESULTADO - TEXTO EN LA FOTO
cv2.putText(foto_prueba,
                f'{resultado} {distancia.round(2)}',
                (50, 50),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                2)

# MOSTRAR IMAGENES
cv2.imshow('Foto A', foto_control)
cv2.imshow('Foto B', foto_prueba)



# MANTENER PROGRAMA ABIERTO
cv2.waitKey(0)
