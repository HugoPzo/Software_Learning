import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QRadioButton, QButtonGroup,  # Radio Buttons Imports
                             QVBoxLayout)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("RADIOBUTTONS")
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        vbox = QVBoxLayout()

        # Set the parent widget to be the window
        payments_group = QButtonGroup(self)
        
        visaButton = QRadioButton("Visa")
        mastercardButton = QRadioButton("Mastercard")
        giftcardButton = QRadioButton("Gift Card")

        # Set Multiple Style Sheet to all Group
        self.setStyleSheet("QRadioButton{"
                           "font-size: 20px;"
                           "color: #000;"
                           "background: #EEE;"
                           "padding: 10px;"
                           "}")


        payments_group.addButton(visaButton)
        payments_group.addButton(mastercardButton)
        payments_group.addButton(giftcardButton)

        payment_location = QButtonGroup(self)

        localPayment = QRadioButton("Local Payment")
        onlinePayment = QRadioButton("Online Payment")

        payment_location.addButton(localPayment)
        payment_location.addButton(onlinePayment)


        vbox.addWidget(visaButton)
        vbox.addWidget(mastercardButton)
        vbox.addWidget(giftcardButton)

        vbox.addWidget(localPayment)
        vbox.addWidget(onlinePayment)

        visaButton.toggled.connect(self.button_changed)
        mastercardButton.toggled.connect(self.button_changed)
        giftcardButton.toggled.connect(self.button_changed)
        localPayment.toggled.connect(self.button_changed)
        onlinePayment.toggled.connect(self.button_changed)

        central_widget.setLayout(vbox)


    def button_changed(self):
        payment = self.sender()
        if payment.isChecked():
            print(f"{payment.text()} is selected!!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()