
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QFrame, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QSpinBox, QGridLayout, QPushButton, QTextEdit
from PyQt6.QtCore import Qt
import functools
import sys

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.food_list = []

        self.lista_comidas = { 
            "Pollo": {"price": 8.50, "amount": 0}, 
            "Cordero": {"price": 15.00, "amount": 0}, 
            "Salmon": {"price": 12.00, "amount": 0}, 
            "Merluza": {"price": 10.50, "amount": 0}, 
            "Kebab": {"price": 6.00, "amount": 0}, 
            "Pizza champiñones": {"price": 9.00, "amount": 0}, 
            "Pizza piña": {"price": 9.50, "amount": 0}
        }

        self.lista_bebidas = {
            "Agua": {"price": 1.50, "amount": 0}, 
            "Soda": {"price": 2.00, "amount": 0}, 
            "Jugo": {"price": 3.00, "amount": 0}, 
            "Cola": {"price": 2.50, "amount": 0}, 
            "Vino": {"price": 7.00, "amount": 0}, 
            "Clericot": {"price": 4.00, "amount": 0}, 
            "Cerveza": {"price": 3.50, "amount": 0}
        }

        self.lista_postres = {
            "Helado": {"price": 4.00, "amount": 0}, 
            "Fruta": {"price": 3.00, "amount": 0}, 
            "Brownies": {"price": 5.00, "amount": 0}, 
            "Flan": {"price": 3.50, "amount": 0}, 
            "Mousse": {"price": 4.50, "amount": 0}, 
            "Pastel": {"price": 6.00, "amount": 0}
        }

        self.calculator_buttons = [ ["7", "8", "9", "+"],
                                    ["4", "5", "6", "-"],
                                    ["1", "2", "3", "*"],
                                    ["C", "0", "=", "/"]]
        
        self.total = ""


        # WINDOW SETTINGS ----------------------------
        # BLOCK RESIZE THE WINDOW
        # self.setFixedSize(1000, 600)
        # .move(x, y) -> Location in Window
        # WINDOW TITLE
        self.setWindowTitle("MI RESTAURANTE - SISTEMA DE FACTURACION")
        # COLOR DE FONDO
        self.setStyleSheet("background: #000;   font-size: 30px;")
        # ---------------------------------------------
        ## WIDGETS

        # Title Label
        self.title_label = QLabel("SISTEMA DE FACTURACION", self)
        # LEFT PANEL ---------------------------------------
        self.left_panel = QVBoxLayout()
        # Menu Panel *****************************************
        self.menu_panel = QHBoxLayout()

        self.menu_foods = QGridLayout()
        self.menu_foods_label = QLabel("Foods", self)

        self.menu_drinks = QGridLayout()
        self.menu_drinks_label = QLabel("Drinks", self)
        
        self.menu_desserts = QGridLayout()
        self.menu_dessert_label = QLabel("Desserts", self)
        # ****************************************************

        # Costs Panel ****************************************
        self.costs_panel = QGridLayout()

        self.costo_comida = QLabel("Costo Comida")
        self.costo_bebida = QLabel("Costo Bebida")
        self.costo_postres = QLabel("Costo Postres")
        self.label_subtotal= QLabel("Subtotal")
        self.label_impuestos = QLabel("Impuestos")
        self.label_total = QLabel("Total")
        # -------------------------------------------
        
        # RIGHT PANEL ---------------------------------------
        self.right_panel = QVBoxLayout()
        # Calculator ***************************************
        self.calculator_total_panel = QVBoxLayout()
        self.calculator_title = QLabel("CALCULATOR")
        self.calculator_lineEdit = QLineEdit(self)
        self.calculator_panel = QGridLayout()

        # **************************************************
        # Receipt ***************************************
        self.receipt = QTextEdit(self)
    

        # **************************************************
        # Buttons ***************************************
        self.buttons_layout = QHBoxLayout()
        self.total_button = QPushButton("Total", self)
        self.receipt_button = QPushButton("Receipt", self)
        self.save_button = QPushButton("Save", self)
        self.reset_button = QPushButton("Reset", self)

        # **************************************************
        # ---------------------------------------------------


        self.initUI()

    def initUI(self):
        # PRINCIPAL LAYOUT
        gbox = QGridLayout()
        
        # Title Label
        gbox.addWidget(self.title_label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("color: #fff;")

        # LEFT PANEL --------------------------------
        gbox.addLayout(self.left_panel, 1, 0)
        self.left_panel.setContentsMargins(15, 15, 15, 15)
        # Menu Panel **************************************
        self.left_panel.addLayout(self.menu_panel)
        
        # Foods
        self.list_food(self.menu_foods_label, self.lista_comidas, self.menu_foods, 1, 0)
        self.menu_panel.addLayout(self.menu_foods)

        # Drinks
        self.list_food(self.menu_drinks_label, self.lista_bebidas, self.menu_drinks, 1, 0)
        self.menu_panel.addLayout(self.menu_drinks)

        # Desserts
        self.list_food(self.menu_dessert_label, self.lista_postres, self.menu_desserts, 1, 0)
        self.menu_panel.addLayout(self.menu_desserts)

        # Costs Panel ***************************************
        self.left_panel.addLayout(self.costs_panel)

        self.costs_panel.addWidget(self.costo_comida, 0, 0)
        self.costs_panel.addWidget(self.costo_bebida, 1, 0)
        self.costs_panel.addWidget(self.costo_postres, 2, 0)
        self.costs_panel.addWidget(self.label_subtotal, 0, 1)
        self.costs_panel.addWidget(self.label_impuestos, 1, 1)
        self.costs_panel.addWidget(self.label_total, 2, 1)
        
        # ****************************************************
        # ---------------------------------------------------

        # RIGHT PANEL -------------------------------------------
        gbox.addLayout(self.right_panel, 1, 1)
        # CALCULATOR *****************************************
        self.right_panel.addLayout(self.calculator_total_panel)

        self.calculator_total_panel.addWidget(self.calculator_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.calculator_total_panel.addWidget(self.calculator_lineEdit)
        self.calculator_lineEdit.setEnabled(False)
        self.calculator_lineEdit.setStyleSheet("color: #fff;")
        self.calculator_total_panel.addLayout(self.calculator_panel)

        self.set_calculator_buttons(self.calculator_panel)
        # ****************************************************

        # Receipt ***************************************
        self.right_panel.addWidget(self.receipt)
        self.receipt.setEnabled(False)
        self.receipt.setContentsMargins(10, 10, 10, 10)
        # ****************************************************

        # Buttons ***************************************
        self.right_panel.addLayout(self.buttons_layout)

        self.buttons_layout.addWidget(self.total_button)
        self.total_button.setStyleSheet("padding: 7px;")
        self.total_button.clicked.connect(self.total_button_func)
        
        self.buttons_layout.addWidget(self.receipt_button)
        self.receipt_button.setStyleSheet("padding: 7px;")
        self.receipt_button.clicked.connect(self.receipt_button_func)
        
        self.buttons_layout.addWidget(self.save_button)
        self.save_button.setStyleSheet("padding: 7px;")
        self.save_button.clicked.connect(self.save_button_func)
        
        self.buttons_layout.addWidget(self.reset_button)
        self.reset_button.setStyleSheet("padding: 7px;")
        self.reset_button.clicked.connect(self.reset_button_func)
        
        # ****************************************************
        

        # ------------------------------------------------------
        


        # SET PRINCIPAL LAYOUT
        self.setLayout(gbox)


    # FOOD METHODS
    def list_food(self, title_label, food_dict, layout, init_row, column):
        layout.addWidget(title_label, 0, 0, Qt.AlignmentFlag.AlignCenter)
        row = init_row
        for food, value in food_dict.items():
            self.checkbox = QCheckBox(f"{food}".capitalize(), self)
            self.spinbox = QSpinBox(self)
            self.spinbox.setEnabled(False)
            layout.setContentsMargins(10, 10, 10, 1)
            layout.addWidget(self.checkbox, row, column)
            layout.addWidget(self.spinbox, row, column+1)
            self.checkbox.setStyleSheet("background-color: #a23; font-size: 10px; color: #fff; padding: 10px;")
            # SEND PARAMETERS WITH A SLOT
            self.checkbox.toggled.connect(functools.partial(self.check_food, food, value["price"], self.spinbox))
            self.spinbox.valueChanged.connect(functools.partial(self.update_food_amount, food_dict, food))
            
            row += 1


    def check_food(self, food, price, spinbox):
        sender_food = self.sender()
        
        if sender_food.isChecked():
            self.food_list.append((food))
            spinbox.setEnabled(True)
            spinbox.setRange(1, 10)
            spinbox.setValue(1)
        else:
            self.food_list.remove((food))
            spinbox.setEnabled(False)
            spinbox.setRange(0, 10)
            spinbox.setValue(0)

        print(self.food_list)

    
    def update_food_amount(self, food_dict, food):
        amount = self.sender()
        food_dict[food]["amount"] = amount.value()
        
        print(food_dict[food])
        
    
    # ----------------------
    # COSTS METHODS
    # ----------------------

    # CALCULATOR METHODS
    def set_calculator_buttons(self, layout):
        row = 0
        column = 0

        for element_row in self.calculator_buttons:
            column = 0
            for element_column in element_row:
                self.button = QPushButton(element_column)
                self.button.clicked.connect(functools.partial(self.calculator_operation))
                layout.addWidget(self.button, row, column)
                column += 1

            row += 1
    
    
    def calculator_operation(self):
        button = self.sender()
        button_text = button.text()
        

        if button_text == "C":
            self.calculator_lineEdit.setText("")
            self.total = ""
        elif button_text == "=":
            try:
                result = str(eval(self.total))
                self.total = result
                self.calculator_lineEdit.setText(result)
            except SyntaxError:
                self.total = ""
                self.calculator_lineEdit.setText("Syntax Error")
            except ZeroDivisionError:
                self.total = ""
                self.calculator_lineEdit.setText("Zero Division Error")
            
        else:
            self.total += button_text
            self.calculator_lineEdit.setText(self.total)
    
    
    # ---------------------- 
    # BUTTONS METHODS - END METHODS
    def total_button_func(self):
        total_food = map()
        total_drink = map()
        total_dessert = map()

        print(total_food)

    
    def receipt_button_func(self):
        print("Receipt")
        


    def save_button_func(self):
        print("Save")


    def reset_button_func(self):
        print("Reset")

    # ----------------------



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()