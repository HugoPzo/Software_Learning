# Python PyQt5 Digital Clock

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
# Module that provides functionality not related to GUI components
from PyQt5.QtCore import QTimer, QTime, Qt
# Module that allow to import customize Fonts
from PyQt5.QtGui import QFont, QFontDatabase

# Digital Clock will be a widget
class DigitalClock(QWidget):

    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        # Timer Variable
        self.timer = QTimer(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("DIGITAL CLOCK")
        self.setGeometry(700, 300, 500, 100)


        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
                                        # All Alingnments are a flag
        self.time_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background: #000;")
        self.time_label.setStyleSheet("""
                                      color: #0F0;
                                      font-weight: 600;
                                      """)
        
        # # Customize the Font
        # Must have a ".TTF" file

                # QFontDatabase - > Class for managing and querying fonts available to the application
        font_id = QFontDatabase.addApplicationFont("/home/hugo/Documentos/Software_Learning/PythonBroCode2/GUI_QT/Projects/DS-DIGIB.TTF")
        # Retrieve the name of the font family from "font_id"
                                    # This Method returns a list of font name
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        # Variable with the font and size
        my_font = QFont(font_family, 100)
        # Set the variable "my_font" to label
        self.time_label.setFont(my_font)


        ## CONNECT OUR TIMER WIDGET TO A SLOT (update_time)
        # During the signal "timeout" connect the slot "update_time"
        self.timer.timeout.connect(self.update_time)
        # Trigger a timeout signal every (ms) time
            # .start(ms)
        self.timer.start(1000)
        self.update_time()


    def update_time(self):
        # Customize the timer
        current_time = QTime.currentTime().toString("hh:mm:ss - AP")
        # Setting the "current_time" to the label
        self.time_label.setText(current_time)



def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()