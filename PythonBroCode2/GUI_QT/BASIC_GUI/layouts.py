# PyQt5 Layouts
import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
                            #         Vertical Box, Horizontal Layout, Grid Layout
                            # These classes deal with layout managers -> They aren't widgets


# We can't add a layout manager to a main window object 
# Main Window widgets have a specific design and layout structure
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    # Create a Generic Widget that can manage layout -> Add layout manager to that widget, then add that widget to Main Window 

    # Keep Organized Code clean & Organized
    # Common Practice 
    def initUI(self):
        # Generic Widget
        central_widget = QWidget() 
        # Add to Main Window -> Generic Widget
        self.setCentralWidget(central_widget)

        # Create Labels
        label1 = QLabel("#1", self)      
        label2 = QLabel("#2", self)      
        label3 = QLabel("#3", self)      
        label4 = QLabel("#4", self)      
        label5 = QLabel("#5", self)

        # Label Styles
        label1.setStyleSheet("background: red")
        label2.setStyleSheet("background: blue")
        label3.setStyleSheet("background: green")
        label4.setStyleSheet("background: brown")
        label5.setStyleSheet("background: yellow")

        ### Layout Manager --------------

        # ## Vertical Layout Manager
        # vbox = QVBoxLayout()
        # # Add Widgets to Layout
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        # ## Set Layout to the generic Widget 
        # central_widget.setLayout(vbox)

        ## Horizontal Layout Manager
        # hbox = QHBoxLayout()
        # # Add Widgets to Layout
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)

        # ## Set Layout to the generic Widget 
        # central_widget.setLayout(hbox)


        ## Grid Layout Manager
        grid = QGridLayout()
        # Add Widgets to Layout
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 2)

        central_widget.setLayout(grid)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()