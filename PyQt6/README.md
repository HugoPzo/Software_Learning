<!-- <h3 style="color:#A23;"></h3> -->

# PyQt6 

## Curso PyQt6

<h3 style="color:#A23;">Creacion de un desarrollo de Entorno</h3>
**Terminal**

`python -m venv "nombre del virtual environment"`

**Seleccionar Interprete del Virtual Environment**
 
    "Ctrl + Shift + P" -> Select Python Interpreter 

**Instalar PyQt6**

`pip3 install pyqt6`

---
<h3 style="color:#A23;">Generación de Ventana</h3>

**Default Structure**

~~~py
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow)

                #QWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Initialize User Interface (Styles, Tools)
    def initUI(self):
        pass
        

    
def main():
    ## QApplication esta encargado de manejar o administrar el "main event loop" (interacciones)
    # Application - sys.argv "Pasar por consola parametros a la aplicacion"                 
    app = QApplication(sys.argv)
    window = MainWindow()
    # Show our window
    window.show()
    # Mainloop, execute the window until a button or action close it
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
~~~
