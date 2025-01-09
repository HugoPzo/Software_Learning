import os
import shutil

print("\n", os.getcwd(), "\n") # C:\Users\hugop\OneDrive\Escritorio\Software_Learning\Udemy\Python16Dias

# archive = open("curso.txt", "w")
# archive.write("TEXTO DE PRUEBA")
# archive.close()

# Get a list from all directories in cwd
print(os.listdir(), "\n") # ['CleanWindow', 'Dia1', 'Dia2', 'Dia3', 'Dia4', 'Dia5', 'Dia6', 'Dia7', 'Dia8', 'DIa9']

# Get user name
print(os.getlogin(), "\n") # hugop

# MOVER ARCHIVOS
# shutil.move("curso.txt")

# # ELIMINA ARCHIVOS
# os.unlink(ruta_archivo) 

# # ELIMINA DIRECTORIOS VACIOS
# os.rmdir(ruta_archivo)

# # ELIMINA DIRECTORIOS COMPLETOS - P.D = CUANDO SE ELIMINA CON ESTE METODO SE ELIMINA POR COMPLETO, NO QUEDA RESTO EN LA PAPELERA DE RECICLAJE
# shutil.rmtree(ruta_archivo)


# # MODULO QUE MANDA A LA PAPELERA
# import send2trash

# send2trash.send2trash(ruta_archivo)


# os.walk(ruta) - > 
# # ALMACENA
# 1: RUTA ACTUAL
# 2: SUBCARPETAS EN RUTA ACTUAL
# 3: ARCHIVOS EN SUBCARPETAS

# CREA TUPLAS POR LOS 3 TIPOS DE INFORMACION
#   (RUTA_ACTUAL, SUBCARPETA, ARCHIVOS)

# # GENERADOR - SE DA LA INFORMACION COMO EL COGIGO LO SOLICITA
print("\n", os.walk(os.getcwd()), "\n") # <generator object _walk at 0x0000017A9AC75E70>

ruta = os.walk(os.getcwd())
# print(next(ruta), "\n") # ('C:\\Users\\hugop\\OneDrive\\Escritorio\\Software_Learning\\Udemy\\Python16Dias', ['CleanWindow', 'Dia1', 'Dia2', 'Dia3', 'Dia4', 'Dia5', 'Dia6', 'Dia7', 'Dia8', 'DIa9'], [])

for carpeta, subcarpeta, archivo in ruta:
    print(f"EN LA CARPETA: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son: ")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")


# for carpeta, subcarpeta, archivo in ruta:
#     print(f"EN LA CARPETA: {carpeta}")
#     print(f"Las subcarpetas son: ")
#     for sub in subcarpeta:
#         print(f"\t{sub}")
#     print("Los archivos son: ")
#     for arch in archivo:
#         # endswith() | startswith()
#         if arch.endswith(".txt"):
#             print(f"\t{arch}")
#     print("\n")
