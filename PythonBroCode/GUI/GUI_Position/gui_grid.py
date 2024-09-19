from tkinter import *

# grid() = geometry manager that organizes widgets in a table-like structure in a

window = Tk()

# Column width depends on the largest widget that it contains

titleLabel = Label(window, text="L O G I N", font=("Montserrat", 20)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First Name", width=20, bg="red").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)


lastNameLabel = Label(window, text="Last Name", width=10, bg="green").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text="Email", width=30, bg="blue").grid(row=3, column=0)
emailEntry = Entry(window).grid(row=3, column=1)


submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()