# PyQt5 Images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

# Importation for handling images and provides functionality for loading, manipulating and displaying images.
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 500, 400)

        # Children of 'window = self' 
        label = QLabel(self)
        label.setGeometry(0, 0, 300, 300)

        # Pixmap to add an image to a label
        # Must add a image inside a label
        pixmap = QPixmap("/home/hugo/Documentos/Software_Learning/PythonBroCode2/GUI_QT/BASIC_GUI/image.jpeg")
        # Set image inside the label
        label.setPixmap(pixmap)
        # Scale image according to the size of the label
        label.setScaledContents(True)

        # Positioning the image - QtCore(Qt) does not work
                                # Same Geometry once set

        ## Bottom Right Corner                        
        # label.setGeometry(self.width() - label.width(), 
        #                   self.height() - label.height(),    
        #                   label.width(), label.height())

        ## Center
        label.setGeometry((self.width() - label.width()) // 2, 
                       (self.height() - label.height()) // 2,    
                        label.width(), label.height())

        ## Etc ...


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())    



if __name__ == "__main__":
    main()