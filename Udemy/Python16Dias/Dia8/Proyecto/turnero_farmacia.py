from numeros import check_system_clean, genera_numero_perfumeria, genera_numero_cosmetico, genera_numero_farmacia, texto_turno

def mostrar_menu():
    print("***************************")
    print("BIENVENIDO - ESCOGA UN AREA")
    print("***************************")

    area_seleccionada = False
    numero_perfumeria = genera_numero_perfumeria()
    numero_farmacia = genera_numero_farmacia()
    numero_cosmetico = genera_numero_cosmetico()

    while not area_seleccionada:

        areas = {"1": "Salir",
                "2": "Perfumeria",
                "3": "Farmacia",
                "4": "Cosmetica"}

        for key, area in areas.items():
            print(f"[{key}] - {area}")

        area_ingresada = input("")

        if area_ingresada not in areas:
            check_system_clean()
            print("Opcion no valida, seleccione un area.")
            continue

        match area_ingresada:
            case "1":
                check_system_clean()
                print("HASTA LUEGO!")
                break
            # Perfumeria
            case "2":
                check_system_clean()
                mostrar_mensaje("P", next(numero_perfumeria))
            # Farmacia
            case "3":
                check_system_clean()
                mostrar_mensaje("F", next(numero_farmacia))
            # Cosmeticos
            case "4":
                check_system_clean()
                mostrar_mensaje("C", next(numero_cosmetico))          


@texto_turno
def mostrar_mensaje(area, numero):
    return print(f"{area} - {numero}")


def main():
    mostrar_menu()


if __name__ == "__main__":
    main()