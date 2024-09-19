from tkinter import *


def submit():
            # text.get(first_line, last_line)
            # first_line = (1.0, 2.0, 3.0, etc...)
            # last_line = (1.0, 2.0, 3.0, or END)
    input = text.get("1.0", END)
    print(input)

# text widget = functions like a text area, you can enter multiple lines of text
#    text widget = text area

window = Tk()

text = Text(window, bg="light yellow",
            # The text area size corresponds to the font size
            # Also ' width & height '
            font=("Ink Free", 25),
            height=8, width=20,
            padx=20, pady=20,
            fg="#A21")

button = Button(window, text="S U B M I T", command=submit)

text.pack()
button.pack()
window.mainloop()