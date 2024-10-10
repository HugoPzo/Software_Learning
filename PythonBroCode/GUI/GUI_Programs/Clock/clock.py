import tkinter.font
from tkinter import *
from time import strftime

window = Tk()
window.config(bg="#000")

def update():
    local_time = strftime("%H:%M:%S")
    time_label.config(text=local_time)

    local_weekday = strftime("%A")
    weekday_label.config(text=local_weekday)

    local_date = strftime("%A - %B - %Y")
    date_label.config(text=local_date)


    # Update the window
            # .after(ms(miliseconds), object_function)
    window.after(1000, update)

time_label = Label(window,
                   bg="#000",
                   fg="#0F0",
                   font=("Georgia", 35))

weekday_label = Label(window,
                   bg="#041",
                   fg="#0F0",
                   font=("Georgia", 25))

date_label = Label(window,
                   bg="#041",
                   fg="#0F0",
                   font=("Georgia", 25))




time_label.pack()
weekday_label.pack()
date_label.pack()

update()


window.mainloop()