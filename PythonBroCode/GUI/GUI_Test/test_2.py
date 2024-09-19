from tkinter import *
from tkinter.ttk import *
import time


def submit_login():
    total_percent = 100
    total_download = 432
    submit_download = 0
    speed = 1

    progress_bar["value"] = 0

    while submit_download < total_download:
        time.sleep(0.05)
        progress_bar["value"] += (speed / total_download) * 100
        submit_download += speed
        # ******************************
        pb.set(f"{int((submit_download/(total_download/total_percent)))}/{total_percent}%")
        tg.set(f"{submit_download}/{total_download}")

        window.update_idletasks()

    print(user_name.get())
    print(password.get())


window = Tk()

# Login ---------------------------
username_label = Label(window, text="User Name", font=("Montserrrat, 15"))
user_name = Entry(window, width=30)
password_label = Label(window, text="Password", font=("Montserrrat, 15"))
password = Entry(window, width=30, show="*")

submit_button = Button(text="SUBMIT", command=submit_login)


# Progress Bar -------------------------
pb = StringVar()
tg = StringVar()

progress_bar = Progressbar(window, length=200)
label_progress_bar = Label(window, textvariable=pb)
label_total = Label(window, textvariable=tg)

username_label.grid(row=0, column=0)
user_name.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password.grid(row=1, column=1)
submit_button.grid(row=2, columnspan=2)
progress_bar.grid(row=4, columnspan=1)
label_progress_bar.grid(row=4, column=1)
label_total.grid(row=4, column=2)

window.mainloop()