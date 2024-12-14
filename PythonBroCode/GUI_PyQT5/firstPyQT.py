# 9:22:20

# PyQT5 introduction

# pip install PyQt5


# This module provides access to some variables
# used or maintained by the interpreter and to
# functions that interact with the interpreter.
# It is always available
# SYSTEM SPECIFIC PARAMETERS AND FUNCTIONS
import sys

# Import Building Blocks from PyQt
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    # All Atributes from 'QMainWindow'
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first PyQt5 GUI")



def main():
    # Object
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exit(app.exec_())


if __name__ == '__main__':
    main()
