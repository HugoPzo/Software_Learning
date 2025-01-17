
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QFrame, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QSpinBox, QGridLayout, QPushButton, QTextEdit, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt
from pathlib import Path
import functools
import sys
import os

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.food_list = []

        self.list_check_spin = []

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
                                    [".", "0", "=", "/"],
                                    ["C"]]
        
        self.total = ""


        # WINDOW SETTINGS ----------------------------
        # BLOCK RESIZE THE WINDOW
        self.setMinimumSize(1200, 600)
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

        self.costo_comida = QLabel()
        
        self.costo_bebida = QLabel()
        
        self.costo_postres = QLabel()
        
        self.label_subtotal= QLabel()
        
        self.label_impuestos = QLabel()
        
        self.label_total = QLabel()
        
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
        self.receipt.verticalScrollBar().maximum()
        self.receipt.setStyleSheet("color: #fff; font-size: 18px;")
        # ****************************************************

        # Buttons ***************************************
        self.right_panel.addLayout(self.buttons_layout)

        self.buttons_layout.addWidget(self.total_button)
        self.total_button.setStyleSheet("padding: 7px;")
        self.total_button.clicked.connect(self.total_button_func)
                
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

    # ----------------------
    # FOOD METHODS
    # ----------------------
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

            self.list_check_spin.append((self.checkbox, self.spinbox))
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

    
    def update_food_amount(self, food_dict, food):
        amount = self.sender()
        food_dict[food]["amount"] = amount.value()
        

    # ----------------------
    # COSTS METHODS
    # ----------------------

    # ---------------------- 
    # CALCULATOR METHODS
    # ---------------------- 
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
    # ---------------------- 
    # Total
    def get_total_value(self, food_dict):
        result = 0
        for item in food_dict.values():
            result += item["price"] * item["amount"]
        
        return result


    def get_item_info(self, item):
        item_price = ""
        item_amount = ""

        if item in self.lista_comidas:
            item_price = self.lista_comidas[item]["price"]
            item_amount = self.lista_comidas[item]["amount"]
        elif item in self.lista_bebidas:
            item_price = self.lista_bebidas[item]["price"]
            item_amount = self.lista_bebidas[item]["amount"]
        elif item in self.lista_postres:
            item_price = self.lista_postres[item]["price"]
            item_amount = self.lista_postres[item]["amount"]

        return item_price, item_amount


    def total_button_func(self):
        total_food = self.get_total_value(self.lista_comidas)
        total_drink = self.get_total_value(self.lista_bebidas)
        total_dessert = self.get_total_value(self.lista_postres)

        costo_subtotal = total_food + total_drink + total_dessert
        costo_impuestos = costo_subtotal * 0.16
        costo_total = costo_subtotal + costo_impuestos

        self.costo_comida.setText(f"Costo Comida - {total_food}")
        self.costo_bebida.setText(f"Costo Bebida - {total_drink}")
        self.costo_postres.setText(f"Costo Postres - {total_dessert}")
        self.label_subtotal.setText(f"Subtotal - {costo_subtotal:.02f}")
        self.label_impuestos.setText(f"Impuestos(IVA) - {costo_impuestos:.02f}")
        self.label_total.setText(f"Total - {costo_total:.02f}")

        # Receipt
        receipt = self.receipt
        receipt.setEnabled(True)
        receipt.verticalScrollBar().setEnabled(True)
        receipt.setText("*"*50)
        receipt.append("Item\tPrice\tAmount\t\tTotal")
        for item in self.food_list:
            price, amount = self.get_item_info(item)
            receipt.append(f'{item}\t${price}\t{amount}\t\t${price*amount}')
        receipt.append("*"*50)        
        
        receipt.append(f"Subtotal:\t\t\t\t ${costo_subtotal:.02f}")        
        receipt.append(f"Impuestos:\t\t\t ${costo_impuestos:.02f}")        
        receipt.append(f"Total:\t\t\t\t ${costo_total:.02f}")        
        
        receipt.append("\n")
        receipt.append("*"*50)        


    # Save
    def save_button_func(self):
        text = self.receipt.toPlainText()
        current_directory = os.getcwd()

        try:

            fname = QFileDialog.getSaveFileName(self,
            "Open File",
            f"{current_directory}",
            "All Files (*);; Python Files (*.py);; Text File (*.txt)", "Text File (*.txt)")
            file_path = Path(fname[0])
            file_path.write_text(text)

            if file_path.exists():
                success_message = QMessageBox().information(self, "Guardado Exitosamente", "Se ha guardado con exito el recibo.")
                
    
        except PermissionError:
            denied_message = QMessageBox().information(self, "Error al guardar", "No se ha podido guardar el recibo.")

    # Reset
    def reset_button_func(self):

        self.costo_comida.setText("")
        self.costo_bebida.setText("")
        self.costo_postres.setText("")
        self.label_subtotal.setText("")
        self.label_impuestos.setText("")
        self.label_total.setText("")

        self.receipt.setText("")
        self.receipt.setEnabled(False)

        self.total = ""
        self.calculator_lineEdit.setText("")

        
        # Clean all checkbox - spinbox
        for checkbox, spinbox in self.list_check_spin:

            checkbox.setChecked(False)

            spinbox.setEnabled(False)
            spinbox.setRange(0, 10)
            spinbox.setValue(0)

    # ----------------------



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()