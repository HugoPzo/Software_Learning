from pathlib import Path, PureWindowsPath
from os import system
import shutil
import os

system("cls")
usuario = os.getlogin()


print("******************************************************")
# User Welcome
print(f"¡¡¡Bienvenido '{usuario.upper()}'!!!")
print("******************************************************\n")

PATH = Path(f"{Path.home()}/OneDrive/Escritorio/Software_Learning/Udemy/Python16Dias/Dia6/Proyecto/Recetas")


# Contador de todas las recetas dentro del directorio
def contador_recetas(path):
    contador = 0
    print("\nRecetas en en el directorio:".upper())
    for receta in path.glob("**/*.txt"):
        print("- ", receta.stem, " -")
        contador += 1
    
    print(f"El Directorio cuenta con {contador} recetas. \n".upper())

# Funcion que permite escoger una categoria y devuelve su 'Path'
def escoger_categoria(path):
    system("cls")
    
    choose_categoria = False

    while not choose_categoria:
        categorias = {}

        print("Categorias Disponibles: ".upper())
        for indice, nombre_receta in enumerate(path.glob("*")):
            print(f"[{indice}]", nombre_receta.stem)
            categorias[indice] = nombre_receta

        user_option = int(input("Choose an option: "))
        
        if user_option not in range(0, len(categorias)):
            system("cls")
            print("Enter a valid option!")
            continue

        ruta_categoria = categorias[user_option]

        choose_categoria = True

    return ruta_categoria

# Funcion que permite escoger una receta y devuelve su 'Path'
def escoger_receta(ruta_categoria):
    # Read Recipe
    system("cls")
    
    choose_receta = False
    # Loop until a recipe has been chosen 
    while not choose_receta:
        try:
            # Print all recipes (basename of)
            print(f"*{os.path.basename(ruta_categoria).upper()}*")
            print("ESCOGE UNA RECETA")

            recetas = {}
            
            for indice, receta in enumerate(ruta_categoria.glob("*")):
                print(f"[{indice}]", receta.stem)
                recetas[indice] = receta

            user_option = int(input("Choose an option: "))
                
            if user_option not in range(0, len(recetas)):
                system("cls")
                print("Enter a valid option!")
                continue
            
            system("cls")

            ruta_receta = Path(recetas[user_option]) 

            choose_receta = True

            return ruta_receta
        
        except ValueError:
            system("cls")
            print("Enter a valid option!")

# Options -------------------------------------------------------------
# Read Recipe
def option_one(path):
    # Category Path
    ruta_categoria = escoger_categoria(path)
    # Recipe Path
    receta = escoger_receta(ruta_categoria)
    # Read text with the recipe path
    print(receta.read_text())
    
# Create New Recipe
def option_two(path):
    ruta_categoria = escoger_categoria(path)

    system("cls")
    receta_created = False
    
    while not receta_created:

        print("ESCRIBE EL NOMBRE DE LA NUEVA RECETA.")
        recipe_name = input("")

        ruta_receta = Path(f"{ruta_categoria}/{recipe_name}.txt")

        if ruta_receta.exists():
            system("cls")
            print("Esa receta ya existe!!".upper())
            continue
        
        system("cls")

        print("INGRESA EL TEXTO QUE IRA DENTRO DE LA RECETA.")
        text_in_recipe = input("")

        ruta_receta.write_text(text_in_recipe)

        receta_created = True

    print(f"{ruta_receta} has been created.")

# Create New Category
def option_three(path):
    system("cls")

    categoria_created = False

    while not categoria_created:
        try:
            # Recibimos nombre de categoria
            print("INGRESA EL NOMBRE DE LA NUEVA CATEGORIA.")
            nombre_categoria = input("")

            # Creamos la ruta + la nueva categoria
            ruta_categoria = path / nombre_categoria
            # Creamos el directorio
            ruta_categoria.mkdir()

            # Cerramos Loop
            categoria_created = True

        except FileExistsError:
            system("cls")
            print("ESA CATEGORIA YA EXISTE.")

# Delete recipe
def option_four(path):
    ruta_categoria = escoger_categoria(path)
    receta = escoger_receta(ruta_categoria)

    os.remove(receta)

    print(f"{receta} has been deleted.")

# Delete category
def option_five(path):
    
    try:
        ruta_categoria = escoger_categoria(path)
        
        os.remove(ruta_categoria)   

        print(f"{ruta_categoria} has been deleted.")   
        
    except PermissionError as error:
        system("cls")
        print("Permission Error.")
        print(error)


# Main ---------------------------------------------------------------
def main():
    print(f"""Ruta de Recetas: '{str(PATH)}'""")    
    contador_recetas(PATH)

    user_option = False

    while not user_option:
        try:
            print("[1] Leer Receta \n[2] Crear Receta \n[3] Crear Categoria \n[4] Eliminar Receta \n[5] Eliminar Categoria \n[6] Exit\n")
            user_option = int(input("Choose an option: "))

            match user_option:
                case 1:
                    option_one(PATH)
                    break
                case 2:
                    option_two(PATH)
                    break
                case 3:
                    option_three(PATH)
                    break
                case 4:
                    option_four(PATH)
                    break
                case 5:
                    option_five(PATH)
                    break
                case 6:
                    user_option = True
                case _:
                    system("cls")
                    print("Enter a valid option!")
                    continue


        except ValueError:
            system("cls")
            print("Enter a valid option!")


if __name__ == "__main__":
    main()