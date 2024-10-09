# 9:29:13

# Animations

from tkinter import *
import time

# Resize IMG
from PIL import Image, ImageTk


# CONSTANTS
WIDTH = 500
HEIGHT = 500

xVelocity = 3
yVelocity = 2

window = Tk()

file = "..\\IMG\\telegram.png"
image = Image.open(file)


canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bg = PhotoImage(file="..\\IMG\\fondo.png")
background = canvas.create_image(0, 0, image=bg, anchor=NW)
# Resize Img                image.resize(tuple(width, height))
telegram_img = ImageTk.PhotoImage(image.resize((50, 50)))
tel_img = canvas.create_image(0, 0, image=telegram_img, anchor=NW)

# Get the image size
image_width = telegram_img.width()
image_height = telegram_img.height()

while True:
    coordinates = canvas.coords(tel_img)
    print(coordinates)



    if (coordinates[0] >= WIDTH-image_width or coordinates[0] < 0 ):
        # Update the coordinates, it gets returned if exceed the limit
        # rest
        xVelocity = -xVelocity
    elif (coordinates[1] >= HEIGHT-image_height or coordinates[1] < 0):

        yVelocity = -yVelocity

    # Move the image
    #     .move(imagen_a_mover, x_update, y_update)
    canvas.move(tel_img, xVelocity, yVelocity)


    # Window is updated
    window.update()
    # Updating Window
    time.sleep(0.01)

window.mainloop()


