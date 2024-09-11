from tkinter import *
# Import Color Choose
# Is a Submodule (reason for second import)
from tkinter import colorchooser

def click():
    # color = colorchooser.askcolor()
    # --------------------------------------
    # color = ((rgb), (hexadecimal color))
    # chosen_color = color[1]
    # --------------------------------------

    # Less Lines
    # window.config(bg=str(color[1]))

    # More less Lines
    window.config(bg=str(colorchooser.askcolor()[1]))



window = Tk()
window.geometry("500x500")
window.config(bg="#000")

button = Button(window, text="C L I C K", command=click)

button.pack()
window.mainloop()