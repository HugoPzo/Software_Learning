from pathlib import Path

# # ruta_base = Path.home()
# # print(ruta_base)

# # ruta = Path("Curso Python", "Día 6", "practicas_path.py")


# ruta = Path(Path.home(), "Curso Python", "Día 6", "practicas_path.py")


# def abrir_leer(ruta):
#     ruta = open(ruta, "r")
#     return ruta.read()


# def sobrescribir(ruta):
#     file = open(ruta, "w")
#     file.write("contenido eliminado")


# def registro_error(archive):
#     file = open(archive, "a")
#     file.write("se ha registrado un error de ejecución")
#     file.close()


ruta = Path(f'{Path.home()}/Desktop/Hola/hola2')
carpeta = ruta.parents[1]
print(carpeta)