# PyQt5 Introduction

import sys 

# Module that provides access to some variables used or mantained by the interpreter and to functions that interact strongly with the inetrepeter. It is always available.

# Window Import                                        Label
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# Font Importation
from PyQt5.QtGui import QFont
# Alignments Importation
from PyQt5.QtCore import Qt

# By Inherit from the parent of 'QMainWindow' we can customize our own windows
class MainWindow(QMainWindow):
    def __init__(self):
        # Call Parent constructor
        super().__init__()

        # Customize window ------
        self.setWindowTitle("My First PyQt5 Label")
        self.setGeometry(700, 300, 500, 500)

        # 'window' is a parent widget
        label = QLabel("Hello GUI", self)
        # Set a Font 'QFont("FontName", Size)'
        label.setFont(QFont("Montserrat", 40))
        # Set Geometry of the label
        label.setGeometry(0, 0, 500, 100)

        # Set Style
        # PyQt have styles that are very similar to CSS
        label.setStyleSheet("color:#FF0000;"
                            "background:#327742;"
                            "font-weight: 600;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # # Set Alignment

        # # Vertically ---------------------

        # # Vertically Top
        # label.setAlignment(Qt.AlignTop)
        # # Vertically Bottom
        # label.setAlignment(Qt.AlignBottom)
        # # Vertically Center
        # label.setAlignment(Qt.AlignVCenter)

        # # Horizontal ---------------------

        # # Horizontal Right
        # label.setAlignment(Qt.AlignLeft)
        # # Horizontal Center
        # label.setAlignment(Qt.AlignHCenter)
        # # Horizontal Left
        # label.setAlignment(Qt.AlignRight)


        # Combine Both (Horizontal | Vertical)
        ## '|' -> Operator(Or, Bitwise)

        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center & Bottom
        label.setAlignment(Qt.AlignRight | Qt.AlignBottom) # Right & Bottom
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop) # Left & Top

        # Center
        label.setAlignment(Qt.AlignCenter)


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