from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton,
                            QLineEdit, QWidget, QVBoxLayout)
from PyQt6.QtCore import Qt
import sys
import requests
from pytemp import pytemp

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter a city name: ", self)
        # Input
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Example: Chicago")

        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel( self)
        
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Weather App 🌥️")
        
        # Set Layout
        vbox = QVBoxLayout()
        # Adding Widgets to label
        vbox.addWidget(self.city_label, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.emoji_label, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.description_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(vbox)

        self.get_weather_button.clicked.connect(self.get_weather)

        # Setting widgets names
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # Setting Style
        self.setStyleSheet("""
        QLabel, QPushButton{
            font-family: Montserrat;
        }

        QLabel#city_label{
            font-size: 40px;
        }

        QLabel#city_input{
            font-size: 40px;
        }

        QLabel#get_weather_button{
            font-size: 30px;
            font-weight: bold;
        }

        QLabel#temperature_label{
            font-size: 75px;
        }

        QLabel#emoji_label{
            font-size: 100px;
            font-family: Segoe UI emoji;
        }

        QLabel#description_label{
            font-size: 50px;
        }
        
        """)

        # font-family: Segoe UI emoji; -> Special family for emojis

    # Get Weather Button Action (slot)
    def get_weather(self):
        
        # URL REQUEST API INFORMATION
        api_key = "api" # OWN API
        city = self.city_input.text()
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


        # Catch Errors
        try: 
            
            # RESPONSE
            response = requests.get(URL)
            # For HTTPError, we have to raise an exception, if any error cannot be catched - MUST TO HANDLE THIS MANUALLY WITH HTTP ERRORS
            response.raise_for_status()
            data = response.json()

            # SHARE INFO IF INFO IS AVAILABLE
            if data["cod"] == 200:
                # SEND DATA RESPONSE TO METHOD
                self.display_weather(data)
        
        # EXCEPTIONS
        except requests.exceptions.HTTPError as http_error:
            # print(response.status_code) # 404, 401, 500, etx...
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nCheck your input.")
                case 401:
                    self.display_error("Unathorized:\nInvalid API Key.")
                case 403:
                    self.display_error("Forbidden:\nAccess denied.")
                case 404:
                    self.display_error("Not Found:\nCity Not Found.")
                case 500:
                    self.display_error("Internal Server Error:\nPlease Try Later.")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid Response from the server.")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down.")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server.")
                
                case _:
                    self.display_error(f"HTTP Error Occured:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Conncetion Error:\nCheck your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck your URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    # DISPLAY ERROR IN WINDOW
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    # DISPLAY WEATHER INFORMARION - EMOJI - TEMPERATURE
    def display_weather(self, data):
        # CONVERT WEATHER INFO INTO CELSIUS OR FARENHEIT
        temperature_k = data["main"]["temp"]
        temperature_c = pytemp(temperature_k, "k", "c")
        temperature_f = pytemp(temperature_k, "k", "f")

        # GET WEATHER ID, DEPENDS ON CITY CONTIDITION
        weather_id = data["weather"][0]["id"]
        # GET WEATHER DESCRIPTION
        weather_description = data["weather"][0]["description"]

        # TEMPERATURE TEXT (CELSIUS, FARENHEIT)
        self.temperature_label.setStyleSheet("font-size: 75px;")
        self.temperature_label.setText(f"{temperature_c:.2f}°C")

        # EMOJI, SEND TO A FUNCTION TO GET A RETURN EMOJI
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

        # SET DESCRIPTION ID
        self.description_label.setText(weather_description.title())

    # GET AN EMOJI DEPENDING THE ID
    @staticmethod
    def get_weather_emoji(weather_id):
        
        if 200 <= weather_id <= 232:
            return "🌩️"
        elif 300 <= weather_id <= 321:
            return "🌧️"
        elif 500 <= weather_id <= 504:
            return "🌦️"
        elif weather_id == 511:
            return "❄️"
        elif 520 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🌨️"
        elif 701 <= weather_id <= 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id == 801:
            return "⛅"
        elif 802 <= weather_id <= 804:
            return "☁️"
        else:
            return ""
        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()