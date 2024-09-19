from tkinter import *

# button = you click it, then it does stuff
count = 0

def click():
    global count # Define the global variable
    count += 1
    print(f"You click {count} times.")


window = Tk()

photo = PhotoImage(file="../IMG/Logo.png")

window.title("Button")

button = Button(window,
                text="Click Me",
                command=click, # Function, action when we use button ---
                                # Define the function as callback, without '()'
                                # command=callback --- Perform a callback
                font=("Comic Sans", 40, "bold"), # Font Style
                fg="#00FF00", # Font Color
                bg="black", # Background
                activeforeground="blue", # Color of text when is clicked
                activebackground="yellow", # Color of backgorund when is clicked
                state=ACTIVE , # Button 'state' can be 'Active' or 'Disabled'
                image=photo,
                compound="bottom"
                )


button.pack()
window.mainloop()