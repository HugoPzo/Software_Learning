import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QPushButton, QLabel)
                            # Button Import


## --------------------  
#   Widget.*signal*.connect(*slot*)
## --------------------

# Widget = Button, Label, etc...

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        ## Button is considered local to our initializer method -> Belongs to the class of 'MainWindow'
        # Without declaring 'self' as prefix we're declaring local variables
        self.button = QPushButton("Click Me!!", self)

        # Label
        self.label = QLabel("Hello", self)

        self.initUI()

    ## A generic widget inside the main Window

    # Initialize User Interface
    def initUI(self):

        ## Button ------
        
        # Button Geometry
        self.button.setGeometry(150, 200, 200, 100)
        # Button Style
        self.button.setStyleSheet("font-size: 20px;")

        ## List a Signal -> A signal is emitted when a widget is interacted it
        # List the type of signal

        # Signal -> Event
        # Slot -> Action

        # Connect Button to Function
        #           signal          (slot)
        self.button.clicked.connect(self.on_click)


        ## Label --------
        self.label.setGeometry(70, 10, 400, 100)
        self.label.setStyleSheet("font-size: 30px;")



    def on_click(self):
        print("Button Clicked")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)

        self.label.setText("You click the Button!!")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()