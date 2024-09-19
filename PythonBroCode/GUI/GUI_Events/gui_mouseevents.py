from tkinter import *

# ALways set the event
def click(event):
    # Button Event --
    # print(event)
    # Button Number --
    # print(event.num)

    #print("You press Something")

    # Coordinates --
    print(f"Coordinates ({event})")
    print(f"Coordinates ({event.x}, {event.y})")

window = Tk()

# Mouse Events -----------------
    # .bind("<event>", function)

# ALl Buttons -----------
#window.bind("<ButtonPress>", click)


# Mouse Button Actions
"""window.bind("<Button-1>", click) # left button
window.bind("<Button-2>", click) # scroll button
window.bind("<Button-3>", click) #right button"""

# Mouse Actions
"""window.bind("<ButtonRelease>", click) # Let out the button"""

# Mouse (I/O) Window
"""window.bind("<Enter>", click) # Enter the window
window.bind("<Leave>", click) # Leave the window """

# All mouse movements in window
window.bind("<Motion>", click)



window.mainloop()