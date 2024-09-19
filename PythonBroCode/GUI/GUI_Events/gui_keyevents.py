from tkinter import *

            # Must pass as argument 'event'
def keyEvent(event):
    print(f"You pressed {event.keysym}")
    label_event["text"] = f"{event.keysym}"

window = Tk()

# Key Bord Event
# ---- Structure
# master.bind("<key>", function)

window.bind("<Key>", keyEvent)

label_event = Label(window, font=("Helvetica", 30))

label_event.pack()
window.mainloop()