from tkinter import *
# import messagebox library
from tkinter import messagebox

def click():

    # --------------------------
    # -- Normal Message Box --
    messagebox.showinfo(title="This is a Info MessageBox", message="Change the click button")
    #messagebox.showwarning(title="This is a Warning MessageBox", message="Warning with the button")
    #messagebox.showerror(title="This is an Error MessageBox", message="Error Error Error!!")

    # Infinite MessageBox
    #while True:
        #messagebox.showerror(title="This is an Error MessageBox", message="Error Error Error!!")

    # -------------------------------------
    #messagebox.askokcancel(title="Ok Cancel", message="Ok or cancel")


    # -------------------------------------
    # -- Info (Ok/Cancel)--

    # True
    #if messagebox.askokcancel():
    #    print("You chose ok")
    # False
    #else:
    #    print("You chose cancel")

    # -------------------------------------
    # -- Warning (Retry/Cancel) --

    # True
    #if messagebox.askretrycancel():
    #    print("You chose retry")
    # False
    #else:
    #    print("You chose cancel")

    # -------------------------------------
    # -- Warning (Yes/No) --

    # True
    # = messagebox.askquestion()
    #if answer == "yes":
    #    print("Yeeeees")
    # False
    #else:
    #    print("Nooooooo")

    # -------------------------------------
    # -- Warning (Yes, No, Cancel) --

    # True, False or None
    # Yes, No, Cancel
    """while True:                         # Could change icons ' warning, error, question, info '
        answer = messagebox.askyesnocancel(icon="question")

        if answer == True:
            print("Yeeeees")
        elif answer == False:
            print("Noooooo")
        else: # Also closing the message box is 'None'
            print("Canceeeeel")"""




window = Tk()


button = Button(window, command=click, text="click me")


button.pack()
window.mainloop()
