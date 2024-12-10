# PyQt5 Introduction

import sys 

# Module that provides access to some variables used or mantained by the interpreter and to functions that interact strongly with the inetrepeter. It is always available.

# Window Import
from PyQt5.QtWidgets import QApplication, QMainWindow
# Icon Importation
from PyQt5.QtGui import QIcon

# By Inherit from the parent of 'QMainWindow' we can customize our own windows
class MainWindow(QMainWindow):
    def __init__(self):
        # Call Parent constructor
        super().__init__()

        # Customize window ------

        # Title
        # self.setWindowTitle("Title")
        self.setWindowTitle("My First GUI PyQt5")
        
        # Geometry
        # self.setGeometry(x, y, width, height)
        self.setGeometry(700, 300, 500, 500)

        # Icon
        # self.setWindowIcon(QIcon("Image Path"))
        self.setWindowIcon(QIcon("./IMG/google.png"))


def main():
    # App Object 
    app = QApplication(sys.argv)
    # Window Object
    window = MainWindow()
    # Show window
    window.show()
    # Exit the system until app object press buttons or any other action
    # Waits around for user input and handles events such as "click buttons, close window, etc..."
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()