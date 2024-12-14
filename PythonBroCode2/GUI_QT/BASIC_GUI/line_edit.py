import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LINE EDIT")
        self.setGeometry(700, 300, 500, 500)

        # Line Edit Widget (Text Box)
        ## Add Line Edit to the window(self)
        self.line_edit = QLineEdit(self)

        # Submit Button
        self.button = QPushButton("SUBMIT", self)

        self.initUI()

        


    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 30)
        self.line_edit.setStyleSheet("font-size: 15px;"
                                     "font-family: Montserrat;")
        self.line_edit.setPlaceholderText("Enter Your Name")
        
        self.button.setGeometry(210, 10, 60, 30)
        self.button.clicked.connect(self.submit)

    
    def submit(self):
        line_edit_text = self.line_edit.text()
        print(f"Hello {line_edit_text}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()