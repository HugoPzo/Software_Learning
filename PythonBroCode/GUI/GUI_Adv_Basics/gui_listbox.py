from tkinter import *

# Functions
def submit():
    # Print Current Selection
    print(list_box.get(list_box.curselection()))
    print(list_box.curselection())

# Add an item from an entry box
def add():
    list_box.insert(list_box.size(), entry_list.get())
    list_box.config(height=list_box.size())


# Delete the current item selection
def delete():
    list_box.delete(list_box.curselection())
    list_box.config(height=list_box.size())


window = Tk()

# ---------------------------------------------------
# List Box

list_box = Listbox(window,
                   bg="#099",
                   width=10,
                   font=("Montserrat", 30))


# Insert the items to the list
foods = ["Pizza", "Tacos", "Sushi", "Pasta"]
for food in foods:
    list_box.insert(list_box.size(), food)

list_box.config(height=list_box.size())


# ---------------------------------------------------
# Buttons

submit_button = Button(window, text="S U B M I T", command=submit)
add_button = Button(window, text="A D D", command=add)
delete_button = Button(window, text="D E L E T E", command=delete)
# ---------------------------------------------------
# Entry

entry_list = Entry(window)


# ---------------------------------------------------
# Pack Elements
list_box.pack()
submit_button.pack()
delete_button.pack()
entry_list.pack()
add_button.pack()

window.mainloop()
