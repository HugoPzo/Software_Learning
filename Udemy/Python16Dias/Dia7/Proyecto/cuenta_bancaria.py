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


class Persona:
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, num_cuenta = 1, balance = 0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance


    def __str__(self):
        return f"***************************************\nNombre: {self.nombre.capitalize()} {self.apellido.capitalize()} \nNumero de Cuenta: {self.num_cuenta} \nBalance: ${self.balance}\n***************************************"

    
    def depositar(self):
        check_system_clean()
        print(self)
        monto_depositado = False
        
        while not monto_depositado:

            try:

                monto = float(input("Ingresa la cantidad a depositar: "))

                if monto <= 0:
                    print("Ingresa una cantidad valida.")
                    continue

                self.balance += monto
                monto_depositado = True

            except ValueError:
                print("Ingrese una cantidad valida.")

        print(self)


    def retirar(self):
        check_system_clean()

        if self.balance == 0:
            print("No cuentas con dinero en tu cuenta.")
            running(self)

        monto_retirado = False

        print(self)

        while not monto_retirado:
            
            try: 
                monto = float(input("Ingresa la cantidad a retirar: "))

                if monto <= 0:
                    print("Ingresa una cantidad valida.")
                    continue
                elif monto > self.balance:
                    print("No puedes retirar esta cantidad, excede tu cuenta.")
                    continue

                self.balance -= monto

                monto_retirado = True
                
            except ValueError:
                print("Ingrese una cantidad valida.")

        print(self)


def pedir_datos():
    print("BIENVENIDO, POR FAVOR INGRESE SUS DATOS.")
    nombre_completo = False

    while not nombre_completo:
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")

        if not nombre.isalpha() or not apellido.isalpha():
            print("Ingresa un nombre valido (Solo letras).")
            continue

        return Cliente(nombre, apellido)


def despedida(cliente):
    check_system_clean()
    print(f"Hasta luego {cliente.nombre}".upper())
    return quit()



def running(cliente):
    opciones = ["y", "n"]

    opcion_completada = False

    while not opcion_completada:
        print("Deseas hacer otra consulta [y/n]: ")
        opcion_usuario = input("").lower()

        if opcion_usuario not in opciones:
            print("Ingresa una opcion valida.")
            continue
        elif opcion_usuario == "n":
            despedida(cliente)
            quit()

        opcion_completada = True

    return menu(cliente)



def menu(cliente):
    check_system_clean()
    print(f"BIENVENIDO {cliente.nombre.upper()}")

    proceso_completado = False

    while not proceso_completado:
        print("[1] Depositar \n[2] Retirar \n[3] Cuenta \n[4] Salir")
        opcion_usuario = input("")

        match opcion_usuario:
            case "1":
                check_system_clean()
                cliente.depositar()
                running(cliente)
            case "2":
                check_system_clean()
                cliente.retirar()
                running(cliente)
            case "3":
                check_system_clean()
                print(cliente)
                running(cliente)
            case "4":
                despedida(cliente)
                proceso_completado = True
            case _:
                print("Ingresa una opcion valida.")
            
            

def main():
    check_system_clean()
    cliente = pedir_datos()
    menu(cliente)


if __name__ == "__main__":
    main()
        