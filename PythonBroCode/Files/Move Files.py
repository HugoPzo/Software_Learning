# +++++++++Move Files+++++++++
import os.path

source = "test.txt" # Or path
destination = "C:\\Users\\hugop\\OneDrive\\Escritorio\\test.txt" # This path is desktop

try:
    if os.path.exists(destination):
        print("There is already a file there...")
    else:
        os.replace(source, destination) # This line move the file or folder (src, dst)
        print(f"{source} was moved")
except FileNotFoundError:
    print(f"{source} was not found.")