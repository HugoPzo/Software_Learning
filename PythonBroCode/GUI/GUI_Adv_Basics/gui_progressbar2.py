from tkinter import *
from tkinter.ttk import *
import time


def download():
    GB = 500
    download = 0
    speed = 2
    while download < GB:
        time.sleep(0.1)
        progress_bar['value'] += (speed /GB) * 100 # 2 / 100 = 0.02 * 100 = 2
        download += speed
        tasks_info.set(f"{download}/{GB} GB completed") # 2 / 100 GB complete
        percent.set(str(int((download/GB)*100)) + "%")  # 2 / 100 = 0.02 * 100 = 2
        window.update_idletasks()

    window.destroy()

window = Tk()

percent = StringVar()
tasks_info = StringVar()

progress_bar = Progressbar(window, length=300, orient=HORIZONTAL)

percentLabel = Label(window, textvariable=percent)
taskLabel = Label(window, textvariable=tasks_info)

download_button = Button(window, text="DOWNLOAD", command=download)


progress_bar.pack()
percentLabel.pack()
taskLabel.pack()
download_button.pack()
window.mainloop()