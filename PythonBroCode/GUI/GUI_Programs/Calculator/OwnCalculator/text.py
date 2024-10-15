from tkinter import * 

window = Tk()

frame = Frame(window)
frame2 = Frame(window)

label = Label(frame, bg="#000", fg="#0F0", text="LABEL")
label.grid(row=0, column=0)
button1 = Button(frame2, width=8, height=5, text=4)
button1.grid(row=0, column=0)
button2 = Button(frame2, width=8, height=5, text=4)
button2.grid(row=1, column=0)
button3 = Button(frame2, width=8, height=5, text=4)
button3.grid(row=2, column=0)
button4 = Button(frame2, width=8, height=5, text=4)
button4.grid(row=3, column=0)

frame.pack(side=TOP)
frame2.pack(side=TOP)
window.mainloop()