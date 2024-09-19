from tkinter import *



window = Tk()

window.config(bg="black")

# radio button = similar to checkbox, but you can only select one from a group
img = PhotoImage(file="../IMG/img.png")
logo = PhotoImage(file="../IMG/Logo.png")
msi = PhotoImage(file="../IMG/msi.png")

images = [img, logo, msi] # List of images, assign an image to each radio button

foods = ["Pizza", "Hamburger", "Tacos"] # Radio Button of food

x = IntVar()

def click_radio():
    for i in range(len(foods)):
        if x.get() == i:
            print(f"You order {foods[i]}")

for index in range(len(foods)):
    radio_button = Radiobutton(window,
                               text=foods[index], # adds text to buttons
                               # * IMPORTANT *
                               variable=x, # groups radio buttons together if they share the same variable
                               value=index, # assign each radiobutton a different value
                               # ************
                               pady=10,
                               font=("Impact", 10),
                               image=images[index], # Assign each radio button an image
                               compound="left", # Set image at left
                               indicatoron=False, # Eliminate 'radio' buttons
                               width=500, # Width of buttons
                               command=click_radio, # Action after clicking a radio button
                               fg="#00FF00",
                               bg="black",
                               activebackground="blue",
                               activeforeground="#CCC",
                               )



    radio_button.pack(anchor=E) # Set button at 'E'ast of the window


window.mainloop()
