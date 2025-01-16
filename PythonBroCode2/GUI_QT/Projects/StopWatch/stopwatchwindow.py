import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel)

from PyQt5.QtCore import  QTime, QTimer, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        # Time Object - QTime(hours, minutes, seconds, miliseconds)
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("START", self)
        self.stop_button = QPushButton("STOP", self)
        self.reset_button = QPushButton("RESET", self)
        self.timer = QTimer(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("STOP WATCH")

        # LAYOUTS & BUTTONS
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label, alignment=Qt.AlignmentFlag.AlignCenter)
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setStyleSheet("""
                           QPushButton, QLable{
                                padding: 20px;
                                font-weight: bold;
                                font-family: Montserrat;
                           }

                           QPushButton{
                                font-size: 30px;
                                color: #843;
                                border: 1px solid #000;
                                border-radius: 6px;
                           }

                           QPushButton:hover{
                                background: #000;
                           }

                           QLabel{
                                font-size: 120px;
                                background: #000;
                                color: #0F0;
                                border-radius: 10px;
                           }""")
        
        # Connect Buttons
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        # Connect Timer
        self.timer.timeout.connect(self.update_display)
    
    
    def start(self):
        # Set an interval for a timeout every 10 miliseconds
        self.timer.start(10)

    def stop(self): 
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
    
    # Return a string with format time
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10 # Get 2 digits

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

     
    def update_display(self):
        # Updating time with 10 miliseconds
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


def main():
                    # "sys.argv" is we are using command line arguments
    app = QApplication(sys.argv)
    stop_watch = Stopwatch()
    stop_watch.show()
            # "exec_()" method is an execute method that starts the main event loop and handles events  
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()