from tkinter import *

try:

    operations = ["+", "-", "/", "*", "BackSpace"]

    window = Tk()
    window["bg"] = "black"
    window.geometry("290x450")
    window.title("CALCULATOR")

    logo = PhotoImage(file="./IMG/IconLogo.png")
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

    numbers = [7, 8, 9, "/", 4, 5, 6, "*", 1, 2, 3, "-", 0, "+"]

    buttons = []
    for n in numbers:

        button = Button(frame,
                      text=n,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",)

        buttons.append(button)

    first_row = [7, 8, 9, "/"]
    second_row = [4, 5, 6, "*"]
    third_row = [1, 2, 3, "-"]
    fourth_row = [0, "+"]

    # --- End Calculator --- Put buttons
    #for m in buttons:







    """button_1 = Button(frame,
                      text=1,
                      height=number_buttons_height,
                      width=number_buttons_width,
                      bg="#000",
                      fg="#0F0",
                      command=operation)"""


    title_label.pack(fill="both")
    results_label.pack(fill="both")
    frame.pack(fill="both")

    window.mainloop()

except KeyboardInterrupt:
    print("You close the window...")


