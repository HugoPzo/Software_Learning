from tkinter import *

window = Tk()


def create_window():
    new_window = Tk() # Toplevel() = new window 'on top' of the other window, linked to the other window
                     # If we close the maste window, both will be closed

    # new_window = Toplevel() # Independent Window, if maste window is closed, the new wont be closed

    window.destroy() # .destroy() will delete the window

Button(text="Create New Window", command=create_window).pack()

window.mainloop()