import numeros

def preguntar():

    print("Bienvenido a Farmacia Python")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmútica")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            # Arroja error si el input no se encuentra en la lista 
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            # Arroja error si el input no se encuentra en la lista 
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()
