from tkinter import *
from tkinter import scrolledtext

# File Menu Functions
def open():
    print("You open the File")

def delete():
    print("You delete the File")

def browse():
    print("You browse the File")


# Edit Menu Functions

def copy():
    print("You copy the file")
def paste():
    print("You paste the file")
def cut():
    print("You cut the file")


# Help Menu Functions
def pls_help():
    print("Pls Help")

window = Tk()

try:
    menuBar = Menu(window) # Create the Menu constructor (Principal Menu) Master = window
    window.config(menu=menuBar, bg="#021") # Configurate the menu in the window

    # MenuBar color cannot be changed

    file_menu = Menu(menuBar, tearoff=False, bg="#000", fg="#0F0") # Create the file menu (Master = menuBar)
    menuBar.add_cascade(label="File", menu=file_menu) # Set cascade to the menu=file_menu inside menubar
    file_menu.add_command(label="Open", command=open)
    file_menu.add_command(label="Delete", command=delete)
    file_menu.add_command(label="Browse", command=browse)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=quit) # or exit

    edit_menu = Menu(menuBar, tearoff=False)
    menuBar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_command(label="Paste", command=paste)
    edit_menu.add_command(label="Cut", command=cut)


    help_menu = Menu(menuBar)
    menuBar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_cascade(label="Pls Heeeeeeeeeeelp", command=pls_help)

    window.mainloop()

except KeyboardInterrupt:
    print("Closing the window...")



