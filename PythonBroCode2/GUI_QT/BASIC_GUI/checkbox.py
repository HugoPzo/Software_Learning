import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QCheckBox)
                                                        # CheckBox Import
# Work with different states
from PyQt5.QtCore import Qt
                                            
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("CHECKBOX")

        self.checkbox = QCheckBox("Do you like food?", self)

        self.initUI()


    def initUI(self):
        # # Give Style & Functionality

        # CheckBox
        self.checkbox.setGeometry(10, 10, 450, 100)
        self.checkbox.setStyleSheet("background: green;"
                                    "padding: 10px;")
        self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(self.check)

    
    def check(self, state):
        # # Check all possibles states
        if state == Qt.Checked:
            print("You like Food!!")
        else:
            print("You DO NOT Like Food!!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()