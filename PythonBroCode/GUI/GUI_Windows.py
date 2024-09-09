from tkinter import *
# tkinter is the GUI package included with python

# widgets = GUI elements: buttons textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

# '()' act as a constructor
# Declare the window
window = Tk()   # instantiate an instance of a window

# Geometry of Interface
window.geometry("500x300") # Declare width x height

# Name of Interface
window.title("Hugo's First GUI") # Title of Interface

# Must convert images to PhotoImage, if we want to add an image
icon = PhotoImage(file="./IMG/Logo.png") # ------

# Change Interface logo
window.iconphoto(True, icon)

# For changes in window, use '.config'
# Example = background="" --- Change background color
window.config(background="black")

# ---------------------------------------------------------------------
# Must be at the end
window.mainloop() # Place window on a computer screen, listen for events
