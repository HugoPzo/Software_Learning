# # ZIPFILE

# import zipfile # Compresion de archivos


# # COMPRIMIR (zipfile) ---------------------------------------------

# ## SI YA EXISTE UNO CON EL MISMO NOMBRE LO SOBRESCRIBE

#             # zipfile.ZipFile("nombre_archivo_zip", "modo_de_apertura")
# mi_zip = zipfile.ZipFile("Archivo_comprimido.zip", "w") # SE CREA "Archivo_comprimido.zip"

# # ARCHIVOS QUE IRAN DENTRO DEL ARCHIVO ZIP
#     # .write("nombre_archivo", "nuevo_nombre_archivo(opcional)")
# mi_zip.write("pruebas_zip1.txt")
# mi_zip.write("pruebas_zip2.txt")

# # CERRAR ARCHIVO
# mi_zip.close()


# # DESCOMPRIMIR (zipfile) ---------------------------------------------

#                                         # Descomprimir con modo 'r'
# zip_abierto = zipfile.ZipFile("Archivo_comprimido.zip", "r")

# # Extraer solo un archivo
# # zip_abierto.extract() # extrae un único archivo (o miembro) del archivo zip, por lo que requiere indicarle cuál de ellos será extraído

# # Extraer todos los archivos
# zip_abierto.extractall()

# zip_abierto.close()

# -----------------------------------------------------------

# # SHUTIL

import shutil
from pathlib import Path

# COMPRIMIR -------------------------------------------
# COMPRIMIR TODOS LOS ARCHIVOS DENTRO DE UNA CARPETA - EN ESTE CASO RECETAS

# RUTA DE ARCHIVO A COMPRIMIR
carpeta_origen = Path("Recetas")

# NOMBRE DEL ARCHIVO COMPRIMIDO - (RUTA) POR DEFAULT ESTA EN LA ACTUAL
carpeta_destino = "Recetas_comprimido"


# HACER EL ARCHIVO CON SHUTIL
# shutil.make_archive(nombre_base(ruta_destino), formato, ruta_del_directorio_a_comprimir)
shutil.make_archive(carpeta_destino, "zip", carpeta_origen) # SE CREA RECETAS_COMPRIMIDO

# DESCOMPRIMIR -------------------------------------------

# shutil.unpack_archive(ruta_nombre_archivo, ruta_nombre_carpeta_descomprimida, formato)
shutil.unpack_archive("Recetas_comprimido.zip", "Recetas_descomprimida", "zip")




