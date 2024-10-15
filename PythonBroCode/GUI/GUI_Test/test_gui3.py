from tkinter import *

try:

    numbers = []
    operations = ["+", "-", "/", "*", "BackSpace"]
    def operation_event(event):
        numbers.append(event.keysym)

        number = ""
        final_number = number.join(numbers)

        result.set(str(final_number))

    def operation():
        pass
        # result = bu

    window = Tk()
    window["bg"] = "black"
    window.geometry("290x450")

    for num in range(10):
        if num == 10:
            num = 0
            window.bind(str(num), operation_event())

        window.bind(str(num), operation_event)


    for sign in operations:
        if sign == "BackSpace":
            window.bind(f"<{sign}>", operation_event)
        window.bind(sign, operation_event)


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



    button_1 = Button(frame,
                      text=1,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)
    button_2 = Button(frame,
                      text=2,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)
    button_3 = Button(frame,
                      text=3,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)
    button_4 = Button(frame,
                      text=4,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)
    button_5 = Button(frame,
                      text=5,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)
    button_6 = Button(frame,
                      text=6,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)
    button_7 = Button(frame,
                      text=7,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)
    button_8 = Button(frame,
                      text=8,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)
    button_9 = Button(frame,
                      text=9,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)
    button_0 = Button(frame,
                      text=0,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)

    divide_button = Button(frame,
                      text="/",
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)

    mult_button = Button(frame,
                      text="x",
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)

    rest_button = Button(frame,
                      text="-",
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)

    sum_button = Button(frame,
                      text="+",
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)

    equal_button = Button(frame,
                        text="=",
                        height=number_buttons_height,
                        width=40,
                        bg="#000",
                        fg="#0F0",
                        command=operation)

    errase_buttom = Button(frame,
                        text="DELETE",
                        height=number_buttons_height,
                        width=40,
                        bg="#000",
                        fg="#0F0",
                        command=operation)



    button_7.grid(row=0, column=0)
    button_8.grid(row=0, column=1)
    button_9.grid(row=0, column=2)
    divide_button.grid(row=0, column=3)
    button_4.grid(row=1, column=0)
    button_5.grid(row=1, column=1)
    button_6.grid(row=1, column=2)
    mult_button.grid(row=1, column=3)
    button_1.grid(row=2, column=0)
    button_2.grid(row=2, column=1)
    button_3.grid(row=2, column=2)
    rest_button.grid(row=2, column=3)
    button_0.grid(row=3, columnspan=3)
    sum_button.grid(row=3, column=3)
    equal_button.grid(rowspan=1, columnspan=4)
    errase_buttom.grid(rowspan=1, columnspan=4)


    title_label.pack(fill="both")
    results_label.pack(fill="both")
    frame.pack(fill="both")

    window.mainloop()

except KeyboardInterrupt:
    print("You close the window...")


