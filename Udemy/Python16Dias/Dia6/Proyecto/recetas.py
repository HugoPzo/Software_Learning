from pathlib import Path
from sys import platform
from os import system
import os

# Check operating system to clean terminal
def check_system_clean():
    # Linux or OS
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        return system("clear")
    # Windows
    elif platform == "win32":
        return system("cls")


system("cls")

usuario = os.getlogin()

check_system_clean()

print("******************************************************")
# User Welcome
print(f"¡¡¡Bienvenido '{usuario.upper()}'!!!")
print("******************************************************\n")

PATH = Path(os.getcwd()) / "Recetas"



# Ask if user wants to continue
def running():

    print("\n")
    answer = False
    answers = ["y", "n"]

    while not answer:
        user_answer = input("Deseas realizar otra consulta? [y/n]: ").lower()

        if user_answer not in answers:
            check_system_clean()
            print("Only [y/n]")
            continue

        if user_answer == "y":
            answer = True
            main()
        else:
            answer = True

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
    check_system_clean()
    
    choose_categoria = False

    while not choose_categoria:
        categorias = {}

        print("Categorias Disponibles: ".upper())
                                                # .iterdir() -> Iterate all Directories
        for indice, nombre_receta in enumerate(path.iterdir()):
            indice = str(indice)
            print(f"[{indice}]", nombre_receta.stem)
            categorias[indice] = nombre_receta

        user_option = input("Choose an option: ").lower()
        
        if user_option in categorias:
            return categorias[user_option]
        else:
            print("Invalid option, please try again.")

# Funcion que permite escoger una receta y devuelve su 'Path'
def escoger_receta(ruta_categoria):
    # Read Recipe
    check_system_clean()
    
    choose_receta = False
    # Loop until a recipe has been chosen 
    while not choose_receta:
        
        # Print all recipes (basename of)
        print(f"*{os.path.basename(ruta_categoria).upper()}*")
        print("ESCOGE UNA RECETA")

        recetas = {}
        recetas_list = list(ruta_categoria.glob("*.txt"))
        
        if not recetas_list:
            print("No hay recetas en esta categoria.")
            return running()

        for indice, receta in enumerate(recetas_list):
            indice = str(indice)
            print(f"[{indice}]", receta.stem)
            recetas[indice] = receta

        user_option = input("Choose an option: ".upper()).lower()
            
        if user_option in recetas:
            return recetas[user_option]
        else:
            print("Invalid option, please try again.")
        

# Options -------------------------------------------------------------
# Read Recipe
def option_one(path):
    # Category Path
    ruta_categoria = escoger_categoria(path)    
    # Recipe Path
    receta = escoger_receta(ruta_categoria)
    # Read text with the recipe path
    print(receta.read_text())

    running()

# Create New Recipe
def option_two(path):
    ruta_categoria = escoger_categoria(path)

    check_system_clean()
    receta_created = False
    
    while not receta_created:

        print("ESCRIBE EL NOMBRE DE LA NUEVA RECETA.")
        recipe_name = input("")

        ruta_receta = Path(f"{ruta_categoria}/{recipe_name}.txt")

        if ruta_receta.exists():
            check_system_clean()
            print("Esa receta ya existe!!".upper())
            continue
        
        check_system_clean()

        print("INGRESA EL TEXTO QUE IRA DENTRO DE LA RECETA.")
        text_in_recipe = input("")

        ruta_receta.write_text(text_in_recipe)

        receta_created = True

    print(f"{ruta_receta} has been created.")

    running()

# Create New Category
def option_three(path):
    check_system_clean()

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
            check_system_clean()
            print("ESA CATEGORIA YA EXISTE.")

    running()

# Delete recipe
def option_four(path):
    ruta_categoria = escoger_categoria(path)
    receta = escoger_receta(ruta_categoria)

    os.remove(receta)

    print(f"{receta} has been deleted.")

    running()

# Delete category
def option_five(path):
    
    try:
        ruta_categoria = escoger_categoria(path)
        
        # Remove Directory (PATH    )
        Path(ruta_categoria).rmdir()

        print(f"{ruta_categoria} has been deleted.")  

        running() 
        
    except PermissionError as error:
        check_system_clean()
        print("Permission Error.")
        print(error)


# Main ---------------------------------------------------------------
def main():
    check_system_clean()
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
                    check_system_clean()
                    print("Enter a valid option!")
                    continue


        except ValueError:
            check_system_clean()
            print("Enter a valid option!")


if __name__ == "__main__":
    main()