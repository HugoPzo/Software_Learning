import sys
from PyQt6.QtWidgets import (QWidget, QApplication, QLineEdit, QLabel, QCheckBox, QPushButton, QMessageBox)
from PyQt6.QtGui import (QFont, QPixmap)
from register import MainWindow

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.register_window = False
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("LOGIN")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        # Variables de instancia -> Accesibles en toda la clase
        self.is_logged = False

        user_label = QLabel("User: ", self)
        user_label.setFont(QFont("Arial", 18, 500))
        # Set widget location
        user_label.move(20, 54)


        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 55)
        self.user_input.setPlaceholderText("Username")
        self.user_input.setFont(QFont("Arial", 14))


        password_label = QLabel("Password: ", self)
        password_label.setFont(QFont("Arial", 18, 500))
        # Set widget location
        password_label.move(20, 90)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)
        self.password_input.move(140, 94)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setFont(QFont("Arial", 14))
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password # Flag, nos facilita la lectura de codigo                   (QLineEdit.EchoMode.Password) = 2
            )
        

        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("Ver contraseña")
        self.check_view_password.move(140, 130)
        self.check_view_password.toggled.connect(self.view_password)


        login_button = QPushButton("Login", self)
        login_button.resize(100, 30)
        login_button.move(130, 160)
        login_button.clicked.connect(self.login)


        register_button = QPushButton("Register", self)
        register_button.resize(100, 30)
        register_button.move(130, 190)
        register_button.clicked.connect(self.register)
        

    def view_password(self, state):
        if state == 0:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)

    def login(self):

        username = self.user_input.text()
        password = self.password_input.text()

        message_box = QMessageBox()

        if username == "hugo" and password == "1234":
            message_box.information(self, "Login Succesful", f"Welcome {username}")
        else:
            message_box.warning(self, "Login Denied", "Wrong User or Password")

    def register(self):
        self.register_window = MainWindow()
        self.register_window.show()
        print(self.register_window)


def main():
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()