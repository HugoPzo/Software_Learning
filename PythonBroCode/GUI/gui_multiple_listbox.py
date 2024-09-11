from tkinter import *

# Functions
def submit():
    # Print Current Selections
    food = []
    for index in list_box.curselection():
        food.insert(index, list_box.get(index))
    print("You order: ")
    [print(i) for i in food]


def add():
    list_box.insert(list_box.size(), entry_list.get())
    list_box.config(height=list_box.size())


def delete():
    # Indexes change if we delete an item, so we reversed it
    for index in reversed(list_box.curselection()):
        list_box.delete(index)

    list_box.config(height=list_box.size())


window = Tk()

# ---------------------------------------------------
# List Box

list_box = Listbox(window,
                   bg="#099",
                   width=15,
                   font=("Montserrat", 15),
                   selectmode=MULTIPLE) # Multiple Selection from the list


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
