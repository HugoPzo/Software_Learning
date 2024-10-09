# 9:11:06
# Drag & Drop
from tkinter import *

def drag_click(event):
    # Declare any widget we made an event
    widget = event.widget
    # Declare the attribute "startX/Y" to the "widget"
    widget.startX = event.x
    widget.startY = event.y

    # Print coordinate inside the widget where it was clicked
    # -- print(widget.startX, widget.startY)

def drag_motion(event):
    widget = event.widget

    # Mathematical calculation where the coordinate will be placed when we drag
    # Example ----
    # x = 8 - 32 + 62 =
    #  x = 38

    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y

    widget.place(x=x, y=y)


    # Return the top left "x" position of the WIDGET in the window
    # -- print(label.winfo_x()) --
    #print(x)
    # Return the top left "y" position of the WIDGET in the window
    # -- print(widget.winfo_y()) --
    #print(y)

window = Tk()

label = Label(window, width=10, height=5, bg="red")
label.place(x=0, y=0)

label_2 = Label(window, width=10, height=5, bg="blue")
label_2.place(x=100, y=100)

# Double bind
label.bind("<Button-1>", drag_click)
label.bind("<B1-Motion>", drag_motion)


label_2.bind("<Button-1>", drag_click)
label_2.bind("<B1-Motion>", drag_motion)

window.mainloop()