# canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *
from turtledemo.penrose import start

window = Tk()

canvas = Canvas(window, height=500, width=500)

                # starting point (x, y), ending point(x, y)
 # Line -------------------
"""canvas.create_line(0, 0, 500, 500)
canvas.create_line(0, 500, 500, 0)
canvas.create_line(0, 250, 500, 250)"""

# Square -----------------

"""canvas.create_rectangle(200, 200, 300, 300, fill="#000")
canvas.create_rectangle(100, 200, 50, 300, fill="#000")
canvas.create_rectangle(310, 200, 500, 300, fill="#000")"""

# Polygons (Triangles, etc...)
            # Sentido de manecillas del reloj
            # starting point (x, y),
"""# canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="green")
points = [250, 0, 500, 500, 0, 500]
canvas.create_polygon(points, fill="red", outline="black", width=10)"""
                                        # outline= Color of line


# Arc "Not a circle" But use sizes of the circle
# What we define is the amount the space we are giving the arc to draw
#                                                   style=CHORD, PIESLICE, ARC

#                                                           start = 90, 180, 270 degrees
"""canvas.create_arc(0, 0, 500, 500, fill="#021", style=CHORD)
canvas.create_arc(0, 0, 500, 500, fill="#128", style=PIESLICE, start=90)
canvas.create_arc(0, 0, 500, 500, fill="#758", style=PIESLICE, start=270)
canvas.create_arc(0, 0, 500, 500, fill="#ABC", style=CHORD, start=180)"""


# Use differents parts of the circle
"""canvas.create_arc(0, 0, 500, 500, fill="#128", style=PIESLICE, start=270, extent=180)"""

# Pokeball
canvas.create_arc(0, 0, 500, 500, extent=180, fill="red", width=10)
canvas.create_arc(0, 0, 500, 500, extent=180, start=180, fill="white", width=10)

# Pokeball Center (Circle)
canvas.create_oval(190, 190, 310, 310, fill="white", outline="black", width=5)


canvas.pack()

window.mainloop()