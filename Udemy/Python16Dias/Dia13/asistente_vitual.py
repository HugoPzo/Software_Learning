import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf # Yahoo Finance
import pyjokes
import webbrowser
import datetime
import wikipedia
import time
from statsbombpy import sb
import json
from pathlib import Path


c_time = datetime.datetime.now()

# ESCUHAR NUESTRO MICROFONO Y DEVOLVER EL AUDIO COMO TEXTO
def transformar_audio_en_texto():

    # ALMACENAR 'RECOGNIZER' EN VARIABLE 
    r = sr.Recognizer()
    
    # CONFIGURAR EL MICROFONO
    with sr.Microphone() as origin:

        # TIEMPO DE ESPERA PARA QUE SE PUEDA ACTIVAR EL MICROFONO - PROBLEMAS DE SONIDO & VOLUMEN SE SOLUCIONEN
        r.pause_threshold = 0.8

        # INFORMAR QUE COMENZO LA GRABACION
        print("Ya puedes hablar!")

        # GUARDAR AUDIO ESCUCHADO
        audio = r.listen(origin)

        # ERRORES
        try:
            # IDENTIFICAR LENGUAJE - TRANSFORMAR A TEXTO
            pedido = r.recognize_google_cloud(audio, language="en-US", credentials_json=r"python-transcription-448615-129e4e304414.json")

            # IMPRIMIR AUDIO ENTENDIDO - PRUEBA DE INGRESO
            print(f"Palabras: {pedido}")

            # DEVOLVER PEDIDO
            return pedido
        
        # EN CASO DE NO COMPRENDER EL AUDIO
        except sr.UnknownValueError:

            # PRUEBA DE NO COMPRENDER EL AUDIO
            print("No se entendio!")

            # DEVOLVER ERROR
            return "Sigo esperando"
        
        # EN CASO DE NO DETECTAR UN MICROFONO
        except OSError:

            print("No se ha detectado un microfono!")

            return "Sigo esperando"
        

        
        # EN CASO DE NO RESOLVER EL PEDIDO
        except sr.RequestError:

            # PRUEBA DE NO PEDIDO NO RESUELTO
            print("No se pudo resolver el pedido!")

            # DEVOLVER ERROR
            return "Sigo esperando"
        
        # # ERROR INESPERADO
        # except:

        #     # PRUEBA DE NO PEDIDO NO RESUELTO
        #     print("Algo ha salido mal!")

        #     # DEVOLVER ERROR
        #     return "Sigo esperando"
        

# FUNCION PARA QUE EL ASISTENTE PUEDA SER ESCUCHADO
def assistant_talks(message):
    # VOCES DISPONIBLES / IDIOMAS
    sabina  = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
    zira = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    david = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    
    # ENCENDER EL MOTOR DE PYTTSX3
    engine = pyttsx3.init()
    # CONFIGURAR LA VOZ
    engine.setProperty('voice', zira)
    

    # PRONUNCIAR MENSAJE
    engine.say(message)
    engine.runAndWait()


# FUNCION QUE GENERA EL SALUDO INICIAL
def saludo_inicial():
    
    # DECIR EL SALUDO
    hour = c_time.hour
    print(hour)

    if hour < 6 or hour > 20:
        moment = "Good Night"
    elif 6 <= hour <= 12:
        moment = "Good Morning"
    else:
        moment = "Good Evening"

    return assistant_talks(f"{moment}, I'm you personal assistant, how can I help you?")


# INFORMAR EL DIA DE LA SEMANA
def pedir_dia():
    
    # CREAR VARIABLE CON DATOS DE HOY
    today = time.strftime("%B %d %Y")
    format_today = f"Today is. {today}"

    return assistant_talks(format_today)


# INFORMAR LA HORA ACTUAL
def pedir_hora():

    # CREAR VARIABLE CON DATOS DE HORA
    current_time = time.strftime("%H:%M %p")
    format_time = f"The time is. {current_time}"

    return assistant_talks(format_time)


# CONTROL DE OPERACIONES
def user_orders():
    saludo_inicial()
    
    running = True

    while running:
        order = transformar_audio_en_texto().lower()

        if "youtube" in order:
            assistant_talks("Starting YouTube!")
            webbrowser.open("www.youtube.com")
            continue
        elif "google" in order:
            assistant_talks("Starting Google!")
            webbrowser.open("www.google.com")
            continue
        elif "day" in order:
            pedir_dia()
            continue
        elif "time" in order:
            pedir_hora()
            continue
        elif "goodbye" in order:
            assistant_talks("GoodBye, see you soon!")
            break
        elif "search in wikipedia" in order:
            assistant_talks("Searching in Wikipedia")
            order = order.replace("search in wikipedia", "")
            # WIKIPEDIA SEARCHING LANGUAGE
            wikipedia.set_lang("en")
            result = wikipedia.summary(order, sentences=1)
            assistant_talks("I get this information in Wikipedia")
            assistant_talks(result)
            continue
        elif "search on internet" in order:
            assistant_talks("Looking on the internet")
            # MODULO PARA BUSCAR EN INTERNET
            pywhatkit.search(order.replace("search on internet", ""))
            assistant_talks("Redirecting you to the Internet, this is what i found")
            continue
        elif "play" in order:
            assistant_talks("Redirecting to YouTube")
            pywhatkit.playonyt(order.replace("play", ""))
            continue
        elif "joke" in order:              # Idioma
            assistant_talks(pyjokes.get_joke("en"))
            continue
        elif "stock price of" in order:
            # SEPARAMOS EL NOMBRE DE LA EMPRESA 
            action = order.split("of")[-1].strip()
            print(action)
            wallet = { 'apple': 'APPL',
                        "amazon": 'AMZN',
                        'google': 'GOOGL'}

            try:
                search_action = wallet[action]
                search_action = yf.Ticker(search_action)
                actual_price = search_action.info['regularMarketPrice']
                assistant_talks(f"I found it, the price of {action} is {actual_price}")
                continue
            except:
                assistant_talks("I'm sorry, I didn't found it.")
                continue


def main():
    user_orders()


if __name__ == "__main__":
    main()