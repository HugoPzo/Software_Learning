from tkinter import *

user_name = "Hugo"

window = Tk()
window.title("Label")

photo = PhotoImage(file="IMG/Logo.png") # Must declare 'PhotoImage' after window constructor


# Create constructor of a label
# window is the 'master' of the label ---- Where does the label will be inserted
label = Label(window, # Master
              text=f"Hello {user_name}, finally you're here", # Text in the label
              font=('Arial', 40, 'bold'), # Font of the text
              fg="#00FF00", # Color of text
              bg="black", # Color of label background
              relief=GROOVE, # Border type
              bd= 5, # Border width
              padx=20, # Padding 'x' label border
              pady=10, # Padding 'y' label border
              image=photo, # Adding a photo to the label
              compound="top", # Where to add the component
              )


# Add the label to 'master window'
label.pack()

# Define specific place for the label
# label.place(x=100)

window.mainloop()
