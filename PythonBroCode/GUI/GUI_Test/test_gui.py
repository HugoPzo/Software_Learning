from tkinter import *
# from tkinter import font
# All fonts in tkinter
"""fonts=list(font.families())
fonts.sort()
print(fonts)"""

def submit():
    print(f"Your user name is {entry_user_name.get()}")
    print(f"Yout passwor is {entry_password.get()}")


def reset():
    entry_user_name.delete(0, END)
    entry_password.delete(0, END)

window = Tk()

window.geometry("400x300")
window.title("Login GUI")
window.config(bg="black")

photo = PhotoImage(file="../IMG/img.png")
window.iconphoto(True, photo)



welcome_label = Label(window,
                      text="Welcome to your Login",
                      font=("Bahnschrift Light SemiCondensed", 20, "bold"),
                      fg="#9c2c24",
                      bg="black",
                      pady=20)


lab_user = StringVar()
lab_user.set("User Name")
username_label = Label(window,
                        textvariable=lab_user,
                        bg="black",
                        fg="#00FF00")


entry_user_name = Entry(window,
                        bg="#CCC",)

lab_pass = StringVar()
lab_pass.set("Password")
password_label = Label(window,
                       textvariable=lab_pass,
                       fg="#00FF00",
                       bg="black")

entry_password = Entry(window,
                       bg="#CCC",
                       show="*")


submit_button = Button(window,
                       text="Submit",
                       fg="white",
                       bg="#0e8f0a",
                       command=submit)



reset_button = Button(window,
                      text="Reset",
                      fg="white",
                      bg="#0e8f0a",
                      command=reset)


welcome_label.pack()
username_label.pack()
entry_user_name.pack()
password_label.pack()
entry_password.pack()
submit_button.place(x=150, y=180)
reset_button.place(x=210, y=180)


window.mainloop()
