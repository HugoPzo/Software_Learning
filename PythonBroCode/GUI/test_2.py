# Making my own Interface


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

window = Tk()

# Window Configurations
# ---------------------------------------
window.config(bg="#000")
window.geometry("500x300")
window.title("My First Login GUI")

icon = PhotoImage(file="IMG/IconLogo.png")
window.iconphoto(True, icon)
# ---------------------------------------

# Menu Bar
# ---------------------------------------
menuBar = Menu(window)
window.config(menu=menuBar)

desktop_path = "C:\\Users\\hugop\\OneDrive\\Escritorio"


def save_file():
    file = filedialog.asksaveasfile(initialdir=desktop_path,
                                    defaultextension=".txt",
                                    filetypes=[(".txt", ".txt"), (".html", ".html")])

    if file == None:
        return

    file.write(input("Write Something"))
    file.close()




def read_file():
    file = filedialog.askopenfilename(initialdir=desktop_path,
                                      filetypes=[(".txt", "*.txt")])

    if file == None:
        return

    try:
        file_text = open(file, "r")
        print(file_text.read())
        file_text.close()
    except FileNotFoundError:
        print(FileNotFoundError)




file_menu = Menu(menuBar)
menuBar.add_cascade(label="File", menu=file_menu)
file_menu.config(tearoff=False)
file_menu.add_command(label="Save File", command=save_file)
file_menu.add_command(label="Read File", command=read_file)
# ---------------------------------------

# Login
# ---------------------------------------
login_frame = Frame(window)
login_frame.place(x=30, y=30)

login_label = Label(login_frame,text="L O G I N", pady=10)


user_name_label = Label(login_frame, text="User Name")
user_name = Entry(login_frame)

password_label = Label(login_frame, text="Password")
password = Entry(login_frame)


# Login Buttons
# ---------------------------------------
def send():
    print(user_name.get())
    print(password.get())


def delete():
    user_name.delete(0, END)
    password.delete(0, END)


width_buttons = 20
send_button = Button(login_frame, text="S E N D", width=width_buttons, command=send)
delete_button = Button(login_frame, text="D E L E T E", width=width_buttons, command=delete)



























# Pack Interface
# ---------------------------------------
login_label.pack(side=TOP)
user_name_label.pack()
user_name.pack()
password_label.pack()
password.pack()
send_button.pack()
delete_button.pack()



window.mainloop()

