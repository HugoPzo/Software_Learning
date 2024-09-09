# +++++++++Delete Files+++++++++
import os
import shutil

path = ("C:\\Users\\hugop\\OneDrive\\Escritorio\\folder")

# os.remove(path) # Remove a file in 'path'
# os.rmdir(path) # Remove a directory in 'path' always there aren't files inside
# os.listdir(path): # If there are files inside, this line will be useful to know
# shutil.rmtree(path) # Remove a directory with files inside, DANGEROUS

try:
    if os.path.exists(path):
        print("This location exists...")
        if os.path.isfile(path):
            os.remove(path)
            print(f"{path} was deleted")
        elif os.path.isdir(path):
            if os.listdir(path):
                print("There are files inside")
                shutil.rmtree(path)
            else:
                os.rmdir(path)
                print(f"{path} was deleted")
    else:
        print("This location doesn't exists")

except FileExistsError as e: # In case the file doesn't exists in the path
    print(f"{e}\nThere is not file here")
except PermissionError as e: # In case we use 'os.remove' with a directory
    print(f"{e}\nYou do not have permission to delete this")
except OSError as e: # In case there are files inside the directory
    print(f"{e}\nYou cannot delete that using that function")


