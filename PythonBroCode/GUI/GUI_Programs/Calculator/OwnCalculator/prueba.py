from Buttons import buttons
from tkinter import *


def create_gui():
    window = Tk()
    window.title("Hugo's Calculator")
    window.geometry("500x500")
    window.config(bg="#000")
    logoImage = PhotoImage(file="logoCalc.png")
    window.iconphoto(True, logoImage)

    return window

WINDOW = create_gui()


def button_click(num):

    labelText = StringVar()
    labelText.set(num)
    label = Label(WINDOW, textvariable=labelText)
    WINDOW.after(1)
    label.pack(side=TOP)
    print(num)


def create_label(window, button):
    label = Label(window, background="#000", fg="#0F0", text=button)
    label.pack(side=TOP)
    return label


def create_frame(window):
    frame = Frame(window)


def create_buttons(frame):
    buttonsText = [7, 8, 9, "/", 4, 5, 6, "*", 1, 2, 3, "-", 0, ".", "+", "="]

    for buttonText in buttonsText:
        #                              Assign the value before it pack it
        button = Button(frame, text=buttonText, command=lambda i=buttonText:button_click(i))
        button.pack()

    return button

def main():
    frame = create_frame(WINDOW)
    button = create_buttons(frame)
    WINDOW.mainloop()

if __name__ == "__main__":
    main()