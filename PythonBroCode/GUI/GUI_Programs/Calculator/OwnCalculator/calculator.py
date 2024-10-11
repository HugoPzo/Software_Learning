from Buttons import buttons
from tkinter import *

def button_num(num):
    print(num)


window = Tk()
window.title("Hugo's Calculator")
window.geometry("500x500")

logo = PhotoImage(file="logoCalc.png")

window.iconphoto(True, logo)

frame = Frame(window)

button1 = Button(frame, width=9, height=4, text=1, command=lambda: button_num(1))
button2 = Button(frame, width=9, height=4, text=2, command=lambda: button_num(2))

frame.pack()
button1.pack()
button2.pack()

window.mainloop()