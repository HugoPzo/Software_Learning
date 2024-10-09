from tkinter import *
import time

from classes.ball import *

window = Tk()


WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

voley_ball = ball(canvas, 0, 0, 100, 0.9, 0.7, "red")
tennis_ball = ball(canvas, 0, 0, 50, 1.2, 0.5, "#0f0")




while True:
    voley_ball.move()
    tennis_ball.move()


    window.update()

window.mainloop()