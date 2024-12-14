# PyQt5 setStyleSheet()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        # Give a name to each widget (Classes/ID on CSS)
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            
            QMainWindow{
                background: #A23;
                }
                      
            QPushButton{
                margin: 25px;
                padding: 10px 30px;
                border: 2px solid #A27;
                border-radius: 10px;
            }
                           
            QPushButton#button1{
                background: #981;
            }
                           
            QPushButton#button2{
                background: #052;
                color: #FFF;
            }
                           
            QPushButton#button3{
                background: #8A3;
            }
                           
            QPushButton#button1:hover{
                background: #881;
            }
                           
            QPushButton#button2:hover{
                background: #781;
                color: #FFF;
            }
                           
            QPushButton#button3:hover{
                background: #753;
            }
            

                           

        """)


        central_widget.setLayout(hbox)
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()