from Buttons import buttons
from tkinter import *

def button_click(num):
    print(num)


# Window Configuration
window = Tk()
window.title("Hugo's Calculator")
window.geometry("500x500")

# Logo GUI
logo = PhotoImage(file="logoCalc.png")
window.iconphoto(True, logo)

# Frame dentro de Window
frame = Frame(window)

# Frame Buttons
buttons = [7, 8, 9, "/", 4, 5, 6, "*", 1, 2, 3, "-", 0, ".", "+", "="]
WIDTH = 8
HEIGHT = 4

for button in buttons:
        
    createButton = Button(frame, width=WIDTH, height=HEIGHT, command=lambda: button_click(button))
    createButton.pack()

frame.pack()

window.mainloop()