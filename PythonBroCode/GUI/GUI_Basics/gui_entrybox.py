import tkinter
from tkinter import *

# entry widget = textbox that accepts a single line of user imput



window = Tk()

window.geometry("800x300")


def submit():
    user_name = entry.get()
    print(f"Hello {user_name}") # If 'submit' button is click, will print what is in the entrybox

def delete():
    entry.delete(0, END) # Delete all from entry box



def backspace():
    entry.delete(len(entry.get())-1, END) # We positionate here
    # Example = "hugoperezort 'i' z" and delete to the end 'z'


# Able the entry box
def active():
    entry.config(state=NORMAL) # Active the entry box


# Disable the entry box
def disable():
    entry.config(state=DISABLED) # Disable the entry box


# Change the entry's box config
def password():
    entry.config(show="*") # When we write, will show only "*" instead of texted word



def unpassword():
    entry.config(show="") # Show the wrote text



# Entry box constructor
entry = Entry(window,
              font=("Arial", 15),
              fg="#00FF00",
              bg="black",
              state=DISABLED)

entry.insert(0, 'SpongeBob') # Default text in entrybox
entry.pack(side=LEFT)


submit_button = Button(window,
                text="submit",
                command=submit,
                fg="#00FF00",
                bg="black")

submit_button.pack(side=RIGHT)

delete_button = Button(window,
                text="delete",
                command=delete,
                fg="#00FF00",
                bg="black")

delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                text="back space",
                command=backspace,
                fg="#00FF00",
                bg="black")

backspace_button.pack(side=RIGHT)


active_button = Button(window,
                text="Active Button",
                command=active,
                fg="#00FF00",
                bg="black")

active_button.pack(side=RIGHT)

disable_button = Button(window,
                text="Disable Button",
                command=disable,
                fg="#00FF00",
                bg="black")

disable_button.pack(side=RIGHT)

password_button = Button(window,
                text="Password Button",
                command=password,
                fg="#00FF00",
                bg="black")

password_button.pack(side=RIGHT)

un_password_button = Button(window,
                text="Unpassword Button",
                command=unpassword,
                fg="#00FF00",
                bg="black")

un_password_button.pack(side=RIGHT)



window.mainloop()