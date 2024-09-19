
from tkinter import *

# Move a label, image, etc...
# Inside the canvas


# Always pass (event) as argument
def move_up(event):
    #           element_to_move inside canvas
    # canvas.move(element_to_move, x, y) -----
    canvas.move(myImage, 0, -10)
def move_down(event):             # Not necessary "+10" only "10"
    canvas.move(myImage, 0, +10)
def move_right(event):
    canvas.move(myImage, +10, 0)
def move_left(event):
    canvas.move(myImage, -10, 0)

window = Tk()

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<d>", move_right)
window.bind("<a>", move_left)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)
window.bind("<Left>", move_left)


canvas = Canvas(window, width=400, height=400)
canvas.pack()

photoImage = PhotoImage(file="avion-de-papel.png")
                        # Coordinates, image=SetImage
        # canvas.create_image(x, y, image=photoImage, anchor=Position in Canvas)
myImage = canvas.create_image(0,0, image=photoImage, anchor=NW)

window.mainloop()