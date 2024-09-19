from tkinter import *

window = Tk()

def check_variable():
    if (x.get() == 1):
        check_button.config(text="I accept it all!!")
    else:
        check_button.config(text="I don't accept it :(")


x = IntVar()

photo = PhotoImage(file="../IMG/img.png")

check_button = Checkbutton(window,
                           text="Please check the box",
                           variable=x,
                           fg="#00FF00",
                           command=check_variable,
                           bg="black",
                           onvalue=1,
                           offvalue=0,
                           activebackground="#CCC",
                           activeforeground="#F32F32",
                           image=photo,
                           compound="left")

check_button.pack()

check_button.mainloop()

window.mainloop()