import os
import tkinter
from tkinter import *
from tkinter import colorchooser, font, filedialog
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter.scrolledtext as scrolledtext


# Button Functions --------------------------------------------------------
def change_color():
    try:
        # Set font color
        text_area.config(fg=str(colorchooser.askcolor(title="Choose Font Color")[1]))
    except tkinter.TclError:
        return


# Must pass '*args' -> Because with 'option Menu' doesnt pass any argument
def change_font(*args):
                     # (Get 'font_name' variable, # Get 'Spinbox' variable)
    text_area.config(font=(font_name.get(), font_size_choser.get()))

# Menu Functions -----------------------------------------------------------

## File Functions

# Get user name
USER_NAME = os.getlogin()
DESKTOP_PATH = f"C:\\Users\\{USER_NAME}\\OneDrive\\Escritorio"


def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension="txt",
                       filetypes=[("Text File", "*.txt"),
                                  ("Python File", "*.py"),
                                  ("Html File", "*.html")],
                       initialdir=DESKTOP_PATH)

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))

            file = open(file, "r")
            text_file = file.readline()
            text_area.insert(1.0, text_file)
            file.close()

        except Exception as e:
            print("File couldn't be open...\n"
                  f"{e}")


def save_file():
    # Save file -----

    #                   Only save the file name
    file = filedialog.asksaveasfilename(initialdir=DESKTOP_PATH,
                                    defaultextension=".txt",
                                    # Default file name
                                    initialfile=".txt",
                                    title="Save File",
                                    filetypes=[("Text File", ".txt"),
                                            ("Python File", ".py"),
                                            ("HTML", ".html")])

    if file is None:
        return

    else:
        # Write text in file
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))
            file.close()
        except Exception as e:
            print(f"File couldn't be save {e}")


def quitWindow():
    window.destroy()


## Edit Functions --------------------------------------------------

#tkinter.Text.event_generate("<<Event>>")

def copy_text():
    text_area.event_generate("<<Copy>>")


def paste_text():
    text_area.event_generate("<<Paste>>")


def cut_text():
    text_area.event_generate("<<Cut>>")


## Help Functions ---------------------------------------------

def about():
    showinfo(title="About Text Editor",
             message="- Text Editor -\n"
                     "By Hugo Perez Ortiz")


# -----------------------------------------------------------------


window = Tk()
window.title("My Text Editor")

# Declare file
file = None

# Set window size
window_width = 500
window_height = 500

# Set window position on screen -> Set in the middle
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# --------------------------------------------------------------

# Text Area

# Set font attributes as a variable -> Deafult Values
font_name = StringVar()
font_name.set("Arial")

font_size = StringVar()
font_size.set("25")

# Set default "font_name" & "font_size"
# Set a 'text area' with a Scroll Bar
text_area = scrolledtext.ScrolledText(window, font=(font_name.get(), font_size.get()))

# Allow text area to expand (Responsive Design)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# 'Text area' should take all of the window
text_area.grid(sticky=N + W + S + E)



# Buttons

frame = Frame(window)
frame.grid()

# Button font color chooser
color_botton = Button(frame, text="Font Color", command=change_color)
color_botton.grid(row=0, column=0)

# Button font family -> Doesn't pass any argument
font_family = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_family.grid(row=0, column=1)

# Button font size choser -> Change 'font size' in text area -> Pass font_size as an argument
font_size_choser = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
font_size_choser.grid(row=0, column=3)


# Menu

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quitWindow)

edit_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Cut", command=cut_text)

help_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)


window.mainloop()
