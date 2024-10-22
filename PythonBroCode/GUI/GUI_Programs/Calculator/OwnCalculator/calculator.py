from tkinter import *

TOTAL_WIDTH = 300
TOTAL_HEIGHT = 537


def create_gui():
    window = Tk()
    window.title("Hugo's Calculator")
    window.geometry(f"{TOTAL_WIDTH}x{TOTAL_HEIGHT}")
    window.config(bg="#000")
    logoImage = PhotoImage(file="logoCalc.png")
    window.iconphoto(True, logoImage)

    return window


WINDOW = create_gui()


def create_label_frame(window):
    frame = Frame(window, width=TOTAL_WIDTH, height=100, relief="ridge", border="5")
    frame.pack(side=TOP)
    return frame


def button_click(num):
    frame = create_label_frame(WINDOW)
    frame.after(1)

    labelText = StringVar()
    labelText.set(num)

    label = Label(frame, textvariable=labelText, fg="#0F0", bg="#000", width=TOTAL_WIDTH, height="100")

    label.pack(side=TOP)

    print(num)


def create_frame(window):
    frame = Frame(window, relief="ridge", border="3")
    frame.pack(side=TOP)
    return frame


def create_buttons(frame):
    WIDTH = 9
    HEIGHT = 5
    buttonsText = [[7, 8, 9, "/"], [4, 5, 6, "*"], [1, 2, 3, "-"], [".", 0, "C", "+"], ["="]]

    row = 0
    for rows in buttonsText:
        column = 0
        for columns in rows:
            #                              Assign the value before it pack it
            button = Button(frame, text=columns, width=WIDTH, height=HEIGHT, fg="#0F0", bg="#000",
                            command=lambda i=columns: button_click(i))
            if columns != "=":
                button.grid(row=row, column=column)
            else:
                button.grid(row=row, columnspan=4)
                button.config(width=40)

            column += 1

        row += 1

    return button


def main():
    create_label_frame(WINDOW)
    frame = create_frame(WINDOW)
    create_buttons(frame)

    WINDOW.mainloop()


if __name__ == "__main__":
    main()