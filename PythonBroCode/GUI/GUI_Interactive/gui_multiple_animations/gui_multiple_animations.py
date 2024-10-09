from tkinter import *
import time

from ball import *


window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()


voley_ball = Ball(canvas, 0, 0, 120, 2, 2, "gray")
tenis_ball = Ball(canvas, 0, 0, 50, 5, 4, "yellow")
basket_ball = Ball(canvas, 0, 0, 200, 3, 4, "orange")
foot_ball = Ball(canvas, 0, 0, 150, 6, 4, "#a21")


while True:
    voley_ball.move()
    tenis_ball.move()
    basket_ball.move()
    foot_ball.move()


    window.update()
    time.sleep(0.01)

window.mainloop()