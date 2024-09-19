from tkinter import *
from tkinter.ttk import *
import time


def download():
    task = 0 # Starting Value
    tasks = 10 # Amount to reach
    while task < tasks:
        time.sleep(1) # Delay print of progressbar

        progress_bar['value'] += 10 # Modifying progressbar value by 10

        task += 1 # How progress will update

        tasks_info.set(f"{task}/{tasks} tasks completed") # Example: 1/10 tasks completed

        percent.set(str(int((task/tasks)*100)) + "%") # 1/10 = 0.1 * 100 = 10%

        window.update_idletasks() # Update progressbar in real time

    window.destroy() # Destroy window when progress end

window = Tk()

# Convert Variable of Labels
percent = StringVar()
tasks_info = StringVar()

progress_bar = Progressbar(window, length=300, orient=HORIZONTAL)

                            # textvariable = Updating Variable
percentLabel = Label(window, textvariable=percent)
taskLabel = Label(window, textvariable=tasks_info)

download_button = Button(window, text="DOWNLOAD", command=download)


progress_bar.pack()
percentLabel.pack()
taskLabel.pack()
download_button.pack()
window.mainloop()