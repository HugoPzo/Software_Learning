from pathlib import Path
import time
import math
import os
import re
from sys import platform
from os import system

# Check operating system to clean terminal
def check_system_clean():
    # Linux or OS
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        return system("clear")
    # Windows
    elif platform == "win32":
        return system("cls")


def busqueda_numserie(ruta_archivos, patron):
    # DIRECTORIO CON TODOS LOS ARCHIVOS DENTRO DE LA RUTA
    directorio = (os.walk(ruta_archivos))

    numeros_serie = []

    # LOOP DENTRO DE LAS CARPETA / ARCHIVOS
    for carpeta, subcarpeta, archivo in directorio:
        # SI EXISTEN ARCHIVOS ACCEDEMOS
        if archivo:
            # ITERAMOS ARCHIVOS
            for arch in archivo: 
                # ABRIMOS LA RUTA AL ARCHIVO
                ruta_archivo = Path(carpeta, arch)

                # LEEMOS CONTENIDO Y BUSCAMOS EL PATRON
                texto_archivo = ruta_archivo.read_text()
                busqueda = re.search(patron, texto_archivo)
                
                # SI ENCONTRAMOS EL PATRON LO AGREGAMOS A LA LISTA JUNTO CON EL NOMBRE DEL ARCHIVO
                if busqueda:
                    arch_numserie = (arch, busqueda.group())
                    numeros_serie.append(arch_numserie)
                
                    
    # RETORNAMOS LISTA
    return numeros_serie


def mostrar_menu(fecha_actual, numeros_serie, tiempo_ejecucion):
    check_system_clean()
    print("----------------------------------------------------")
    print(f"Fecha de busqueda: {fecha_actual}\n")
    print("ARCHIVO\t\t\tNRO. SERIE")
    print("-------\t\t\t----------")
    for archivo, no_serie in numeros_serie:
        print(f"{archivo}\t\t{no_serie}")

    print(f"\nNumeros encontrados: {len(numeros_serie)}")
    print(f"Duracion de la busqueda: {tiempo_ejecucion} segundos")
    print("----------------------------------------------------")


def main():
    # CONTAMOS EL TIEMPO DE EJECUCION
    inicio = time.time()

    # RUTA ARCHIVOS
    ruta_archivos = Path("C:/Users/hugop\OneDrive/Escritorio/Software_Learning/Udemy/Python16Dias/Dia9/Proyecto/Mi_Gran_Directorio")
    patron = "N\D{3}-\d{5}"

    # NUMEROS DE SERIE ENCONTRADOS
    numeros_serie = busqueda_numserie(ruta_archivos, patron)

    # FECHA Y HORA ACTUAL
    fecha_actual = time.strftime("%d/%m/%Y a las %H:%M:%S")

    final = time.time()

    # TOTAL DE TIEMPO DE EJECUCION
    tiempo_ejecucion = math.ceil(final - inicio)

    mostrar_menu(fecha_actual, numeros_serie, tiempo_ejecucion)


if __name__ == "__main__":
    main()