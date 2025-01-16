
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QFrame, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QSpinBox
from PyQt6.QtCore import Qt 
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # WINDOW SETTINGS ----------------------------
        # BLOCK RESIZE THE WINDOW
        self.setFixedSize(1000, 600)
        # .move(x, y) -> Location in Window
        # WINDOW TITLE
        self.setWindowTitle("MI RESTAURANTE - SISTEMA DE FACTURACION")
        # COLOR DE FONDO
        self.setStyleSheet("background: #023;   font-size: 30px;")
        # ---------------------------------------------

        # TITLE LABEL -------------------------------
        self.title_label = QLabel("Mi Restaurante - Sistema de Facturacion", self)
        self.title_label.setStyleSheet("border: 2px solid #fff; border-radius: 10px; padding: 5px 50px;")
        # --------------------------------------------

        # PANEL IZQUIERDO
        self.left_panel = QFrame()
        self.left_panel.setStyleSheet("border: 2px solid #fff")
        # PANELES DENTRO DE PANEL IZQ
        # PANEL MENU
        self.menu_panel = QFrame()
        # WIDGETS INSIDE MENU PANEL
        self.food_panel = QVBoxLayout()
        self.lista_comidas = {
                            "Pollo": 8.50, 
                            "Cordero": 15.00, 
                            "Salmon": 12.00, 
                            "Merluza": 10.50, 
                            "Kebab": 6.00, 
                            "Pizza champiñones": 9.00, 
                            "Pizza piña": 9.50
                            }   
        self.drink_panel = QVBoxLayout()
        self.lista_bebidas = {
                            "Agua": 1.50, 
                            "Soda": 2.00, 
                            "Jugo": 3.00, 
                            "Cola": 2.50, 
                            "Vino": 7.00, 
                            "Clericot": 4.00, 
                            "Cerveza": 3.50
                        }
        self.dessert_panel = QVBoxLayout()
        self.lista_postres = {
                            "Helado": 4.00, 
                            "Fruta": 3.00, 
                            "Brownies": 5.00, 
                            "Flan": 3.50, 
                            "Mousse": 4.50, 
                            "Pastel": 6.00
                        }
        # PANEL COSTO
        self.costs_panel = QFrame()

        # PANEL DERECHO
        self.right_panel = QFrame()
        self.right_panel.setStyleSheet("border: 2px solid #fff")
        # PANELES DENTRO DE PANEL DER
        self.calculator_panel = QFrame()
        self.receipt_panel = QFrame()
        self.buttons_panel = QFrame()
        self.initUI()


    def initUI(self):
        # PRINCIPAL PANEL ----------------------------
        vbox = QVBoxLayout()
        # ADD TITLE LABEL ---------------------------
        vbox.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignCenter, stretch=1)
        # ----------------------------------------


        # PANELS
        panel_hbox = QHBoxLayout()

        # LEFT PANEL
        panel_hbox.addWidget(self.left_panel)
        v_left_panel = QVBoxLayout()
        
        # ADD LEFT PANEL WIDGETS
        # SET MENU PANEL
        v_left_panel.addWidget(self.menu_panel)
        # MENU PANEL
        menu_panel_layout = QHBoxLayout()
        
        # FOOD
        menu_panel_layout.addLayout(self.food_panel)
        self.food_label = QLabel("Food", self)
        self.food_label.setStyleSheet("border: 0px; font-size: 20px;")
        self.food_panel.addWidget(self.food_label, alignment=Qt.AlignmentFlag.AlignCenter)
        for food, price in self.lista_comidas.items():
            self.button = QCheckBox(f"{food} - {price}", self)
            self.button.setStyleSheet("font-size: 10px; padding: 10px;")
            self.button.toggled.connect(self.check_food)
            self.food_panel.addWidget(self.button)
        
        # DRINK
        menu_panel_layout.addLayout(self.drink_panel)
        self.drink_label = QLabel("Drink", self)
        self.drink_label.setStyleSheet("border: 0px; font-size: 20px;")
        self.drink_panel.addWidget(self.drink_label, alignment=Qt.AlignmentFlag.AlignCenter)
        for drink, price in self.lista_bebidas.items():
        # DESSERTS
            self.button = QCheckBox(f"{drink} - {price}".capitalize(), self)
            self.button.setStyleSheet("font-size: 10px; padding: 10px;")
            self.button.toggled.connect(self.check_food)
            self.drink_panel.addWidget(self.button)
        
        # DESSERT
        menu_panel_layout.addLayout(self.dessert_panel)
        self.dessert_label = QLabel("Dessert", self)
        self.dessert_label.setStyleSheet("border: 0px; font-size: 20px;")
        self.dessert_panel.addWidget(self.dessert_label, alignment=Qt.AlignmentFlag.AlignCenter)
        for dessert, price in self.lista_postres.items():
            self.button = QCheckBox(f"{dessert}  - {price}".capitalize(), self)
            self.button.setStyleSheet("font-size: 10px; padding: 10px;")
            self.button.toggled.connect(self.check_food)
            self.dessert_panel.addWidget(self.button)
        self.menu_panel.setLayout(menu_panel_layout)

        # SET COSTS PANEL
        v_left_panel.addWidget(self.costs_panel)
        # SET LEFT PANEL LAYOUT
        self.left_panel.setLayout(v_left_panel)
    

        # RIGHT PANEL
        panel_hbox.addWidget(self.right_panel)
        v_right_panel = QVBoxLayout()
        # ADD RIGHT PANEL WIDGETS
        v_right_panel.addWidget(self.calculator_panel)
        v_right_panel.addWidget(self.receipt_panel)
        v_right_panel.addWidget(self.buttons_panel)
        
        # SET RIGHT PANEL LAYOUT
        self.right_panel.setLayout(v_right_panel)

        # ADD HORIZONTAL LAYOUT IN PRINCIPLE PANEL
        vbox.addLayout(panel_hbox, stretch=10)

        # SET PRINCIPAL LAYOUT
        self.setLayout(vbox)


    def check_food(self):
        food = self.sender()

        if food.isChecked():
            print(f"{food.text()}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()