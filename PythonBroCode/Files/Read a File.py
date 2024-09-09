# +++++++++Read a File+++++++++

path = "C:\\Users\\hugop\\OneDrive\\Imágenes\\test.txt"


# This code works, with 'open()' the file will be open and closed automacally
# But it won't catch and handle any exceptions, so we need to...
with open(path) as file:
    print(file.read())


# Best way to open a File
try:
    with open(path) as file:
        print(file.read())
except FileExistsError as e:
    print(e)
    print("The file wasn't found :(")

