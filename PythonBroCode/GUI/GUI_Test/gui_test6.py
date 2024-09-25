from tkinter import *
try:

    def operation():
        print(button.grid_info())

    window = Tk()
    window["bg"] = "black"
    window.geometry("401x473")
    window.title("CALCULATOR")

    logo = PhotoImage(file="../IMG/IconLogo.png")
    window.iconphoto(True, logo)


    result = StringVar()

    title_label = Label(window,
                          text="C A L C U L A T O R",
                          font=("Montserrat", 20),
                          padx=5,
                          pady=5,
                          bg="black",
                          fg="#0F0")

    results_label = Label(window,
                          textvariable=result,
                          bg="#111",
                          borderwidth=10,
                          height=3,
                          relief=SUNKEN,
                          fg="#0F0",
                          font=("Montserrat", 10))

    frame = Frame(window,
                  bg="#111",
                  height=3,
                  width=3)


    number_buttons_width = 9
    number_buttons_height = 3

    buttons = []
    row = 0
    for elements in calculator_elements:
        column = 0
        for element in elements:
            button = Button(frame,
                            text=element,
                            height=number_buttons_height,
                            width=number_buttons_width,
                            bg="#000",
                            fg="#0F0",
                            command=operation,)

            if button["text"] == 0:
                button.grid(row=row, columnspan=3)
                column += 2
            elif button["text"] == "CA":
                button.grid(row=row, column=column)
                column += 2
            else:
                button.grid(row=row, column=column)

            buttons.append(button)

            column += 1
        row += 1

    button_dict = {}
    for button in buttons:
        # pass each button's text to a function
        def action(x=button):
            return text_updation(x)


        # create the buttons
        button_dict[button] = Button(root, text=button,)




    title_label.pack(fill="both")
    results_label.pack(fill="both")
    frame.pack(fill="both")

    window.mainloop()

except KeyboardInterrupt:
    print("You close the window...")
=======
for i in range(1000000):
    print(i)
>>>>>>> Stashed changes
