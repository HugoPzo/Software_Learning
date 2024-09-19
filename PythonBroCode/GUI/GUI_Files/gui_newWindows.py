from tkinter import *

window = Tk()


def create_window():
    #new_window = Tk() # Independent Window, if master window is closed, the new wont be closed


    new_window = Toplevel() # Toplevel() = new window 'on top' of the other window, linked to the other window
                     # If we close the master window, both will be closed

    #window.destroy() # .destroy() will delete the window

Button(text="Create New Window", command=create_window).pack()

window.mainloop()