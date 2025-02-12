import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QHBoxLayout, QStyleFactory)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.login_button = QPushButton("Login")
        self.initUI()


    def initUI(self):
        self.setWindowTitle("LOGIN")
        # Lock resize of the window
        self.setFixedSize(300, 200)

        vbox = QVBoxLayout()

        # Login Image ------------------------------------------------------------
        pixmap = QPixmap(r"C:\Users\hugop\OneDrive\Escritorio\Software_Learning\PyQt6\Login\iniciar-sesion.png").scaled(50, 50)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        # Align in Center
        vbox.addWidget(image_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Login ------------------------------------------------------------
        
        # User Name
        username_layout = QHBoxLayout()

        username_text = QLabel("UserName: ")
        username_layout.addWidget(username_text)
        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText("UserName")
        self.username_entry.setObjectName("login_entry")
        username_layout.addWidget(self.username_entry)
        vbox.addLayout(username_layout)

        # Password

        password_layout = QHBoxLayout()

        password_text = QLabel("Password: ")
        password_layout.addWidget(password_text)
        self.password_entry = QLineEdit()
        self.password_entry.setPlaceholderText("Password")
        # Hide Password
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_entry.setObjectName("login_entry")
        password_layout.addWidget(self.password_entry)

        vbox.addLayout(password_layout)


        # Login Button
        self.login_button.clicked.connect(self.handle_login)
        vbox.addWidget(self.login_button)

        # ----------------------------------------------


        self.setLayout(vbox)

        self.setStyleSheet("""
                            QLineEdit#login_entry{
                                width: 200px;
                            }

                        """)    


    def handle_login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        # MessageBox
        message = QMessageBox()

        if username == "admin" and password == "1234":
            message.information(self, "Login Succesful", f"Welcome {username}!")
        else:
            message.warning(self, "Wrong Failed", "Invalid username or password.")
            
        


def main():
    # Método que toma todas las interacciones que el usuario haga con la aplicacion, pasa una lista de argumentos
    app = QApplication(sys.argv)
    # # Set Application style (default black)
    # print(QStyleFactory.keys()) ['windows11', 'windowsvista', 'Windows', 'Fusion']
    app.setStyle("windowsvista")
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()