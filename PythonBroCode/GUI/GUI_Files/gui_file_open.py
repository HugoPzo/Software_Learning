from tkinter import *
# Must import 'filedialog' submodule
from tkinter import filedialog

def openfile():
                                            # initialdir = Where it be the deafult path open
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\hugop\\OneDrive\\Imágenes",
                                           title="Open a Text File",
                                           # Delimit what type of files can be open
                                           # filetypes = [("message appear", "*.extension")]
                                           # * = Means "all"
                                           # Example = *.* -> all names with all extensions
                                           filetypes=[(".txt", "*.txt"), (".all", "*.*")]
                                           )


    file = open(file_path, "r")
    print(file.read())

    # Must to close file **
    file.close()



    # Return File Path
    # print(file)


window = Tk()



button = Button(window, text="O P E N", command=openfile)


button.pack()
window.mainloop()