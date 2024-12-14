# # Scale a Pixmap(Image), must to create a copy
#     pixmap = QPixmap(f"/home/{os.getlogin()}/Documentos/Software_Learning/PythonBroCode2/GUI_QT/IMG/google.png")
#     pixmap_scaled = pixmap.scaled(50, 150)

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,QLabel, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 800, 500)
        self.setWindowTitle("My Test GUI")
        self.button = QPushButton("YOU CLICK THE BUTTON")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        # LABEL -----------------------------------        
        label = QLabel("Welcome to Horizontal")
        label.setStyleSheet("color: #fff;"
                            "background: black;")
        
        label.setAlignment(Qt.AlignCenter)
        hbox.addWidget(label)

        # BUTTON -----------------------------------
        
        # Connect Button event to method
        self.button.clicked.connect(self.on_click)
        # Align Button
        hbox.addWidget(self.button, alignment=Qt.AlignCenter)
    
        # IMAGE ------------------------------------
        image_label = QLabel()
        pixmap = QPixmap("/home/hugo/Documentos/Software_Learning/PythonBroCode2/GUI_QT/BASIC_GUI/image.jpeg")
        rescaled_pixmap = pixmap.scaled(100, 100)
        image_label.setPixmap(rescaled_pixmap)
        # Align an image inside a layout
        hbox.addWidget(image_label, alignment=Qt.AlignCenter)


        # CheckBox --------------------------------
        self.checkbox = QCheckBox("Hi! Are you there??")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.isChecked)
        hbox.addWidget(self.checkbox, alignment=Qt.AlignCenter)
        

        # # Radio Buttons -------------------------------
        # Create Vertical Layout for Radio Buttons
        v_rb_box = QVBoxLayout()
        # Radio Buttons Group
        foodGroup = QButtonGroup()
        # Radio Buttons Creation
        radioButton1 = QRadioButton("Pizza")
        radioButton2 = QRadioButton("Sushi")
        radioButton3 = QRadioButton("Tacos")
        # Adding Buttons to the group
        foodGroup.addButton(radioButton1)
        foodGroup.addButton(radioButton2)
        foodGroup.addButton(radioButton3)
        # Adding Buttons to Vertical layout
        v_rb_box.addWidget(radioButton1, alignment=Qt.AlignCenter)
        v_rb_box.addWidget(radioButton2, alignment=Qt.AlignCenter)
        v_rb_box.addWidget(radioButton3, alignment=Qt.AlignCenter)
        # Connect Buttons to method
        radioButton1.toggled.connect(self.buttonSelected)
        radioButton2.toggled.connect(self.buttonSelected)
        radioButton3.toggled.connect(self.buttonSelected)
        
        # Adding Vertical Buttons Layout to Horizontal Layout
        hbox.addLayout(v_rb_box)


        # Line Edit -----------------------------------------
        text_submit_ly = QVBoxLayout()
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter Your Name")
        text_submit_ly.addWidget(self.line_edit, alignment=Qt.AlignCenter)
        submit_button = QPushButton("SUBMIT")
        submit_button.clicked.connect(self.submit)
        text_submit_ly.addWidget(submit_button, alignment=Qt.AlignCenter)
        
        hbox.addLayout(text_submit_ly)
        
        central_widget.setLayout(hbox)



    def on_click(self):
        print("You click the button!!")
        
    def isChecked(self, state):
        if state == Qt.Checked:
            print("Checked!!")
        else:
            print("Not checked!!")
    
    def buttonSelected(self):
        sender = self.sender()
        ## Which radio button send the signal
        # Must add verification, if not, sender will send last and new buttons information
        if sender.isChecked():
            print(f"{sender.text()} selected!!")


    def submit(self):
        text = self.line_edit.text()
        print(f"Hi {text}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
