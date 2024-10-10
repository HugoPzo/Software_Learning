import tkinter.font
from tkinter import *
import time

window = Tk()

window.config(background="#000")

print(tkinter.font.families())

while True:
    local_t = time.localtime()
    time_act = time.strftime("%A - %d/%B/%Y - %H:%M:%S %p", local_t)

    date = StringVar()
    date.set(time_act)
    timeLabel = Label(window,
                      textvariable=date,
                      fg="#0f0",
                      bg="#000",
                      font=("Georgia", 30))
    timeLabel.pack()

    window.update()
    time.sleep(1)
    timeLabel.destroy()

window.mainloop()