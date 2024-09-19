from tkinter import *

# scale of numbers

def temperature():
    print(f"The temperature is {scale.get()} degrees...") # Print value set in scale

window = Tk()
window.config(bg="black")

image_1 = PhotoImage(file="../IMG/Logo.png")
image_2 = PhotoImage(file="../IMG/img.png")

label_1 = Label(window, image=image_1)
label_2 = Label(window, image=image_2)

scale = Scale(window,
              from_=450, to=-50,
              length=400,
              tickinterval=10, # Adds numeric indicators for value
              orient=VERTICAL, # Scale's orientation
              resolution= 5, # Increment of slider
              troughcolor="#00AEEA",
              showvalue=True, # Show value of scale
              sliderrelief="flat",
              bg="black",fg="#00FF00",
              )



scale.set(((scale["from"]-scale["to"])/2)+scale["to"]) # Set current position of slider
                                    # +scale["to"] just in case is greater than zero

button = Button(window,
                text="Submit",
                command=temperature,)

label_1.pack()
scale.pack()
label_2.pack()
button.pack()
window.mainloop()
