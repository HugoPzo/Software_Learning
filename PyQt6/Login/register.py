import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("MY FIRST WINDOW")
        self.setStyleSheet("""QMainWindow{
                                background: #fff;
                            }""")

    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()