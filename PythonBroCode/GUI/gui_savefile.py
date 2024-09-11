from tkinter import *
from tkinter import filedialog


def saveFile():                     # Default open path
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\hugop\\OneDrive\\Escritorio",
                                    # default save extension
                                    defaultextension=".txt",
                                    # Types of extension it can be saved
                                    filetypes=[("Text File", ".txt"),
                                               ("HTML", ".html")])

    # If file Interface is closed, this lines prevents to get an error
    if file is None:
        return
    # -----------------------------------------------------------

    file_text = text.get(1.0, END) # Get Info from the text area
    file.write(file_text) # Write the text from text_area to the file
    file.close() # Close the file




window = Tk()

text = Text(window)
button = Button(window, text="S A V E", command=saveFile)

text.pack()
button.pack()

window.mainloop()