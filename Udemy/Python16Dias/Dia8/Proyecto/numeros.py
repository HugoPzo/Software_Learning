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


# DECORADORES Y GENERADOR

# DECORADOR - TEXTO POR TURNO
def texto_turno(funcion):

    def imprime_texto(area, numero):
        print(f"Tu turno es:")
        funcion(area, numero)
        print("Aguarde un momento...\n")

    return imprime_texto


# GENERADOR - TURNO POR AREA

def generador():
    turno = 1
    while True:
        yield turno
        turno += 1


# Generator within generator
def genera_numero_perfumeria():
    # Yield from <generator_name>
    yield from generador()


def genera_numero_farmacia():
    yield from generador()


def genera_numero_cosmetico():
    yield from generador()



