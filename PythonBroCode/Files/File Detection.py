# +++++++++File Detection+++++++++

import os

# (\\) Represent on back slash in directory
path = "C:\\Users\\hugop\\OneDrive\\Imágenes\\test.txt"

# Print the path to the last location
print(os.path.dirname(path))

if os.path.exists(path):
    print("This location exists!!")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("This is a directory!")
else:
    print("That location doesn't exist!")