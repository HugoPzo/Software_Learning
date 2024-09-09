from tkinter import *


window = Tk()

def click():
    name = entry.get()
    label.config(text=f"Hola {name}") # Change text in label

entry = Entry(window,)
entry.pack()

label = Label(window,text="Hola como estas")
label.pack()

button_label = Button(window,text="change label", command=click)
button_label.pack()

# ----------------------------------------------------------------------
def button_click():
    name.set("Hello Variable")

name = StringVar()
name.set("Hello World") # Change text with an event (variable)

label_2 = Label(window,textvariable=name)
label_2.pack()

button_variable = Button(window, text="change variable", command=button_click)
button_variable.pack()

window.mainloop()