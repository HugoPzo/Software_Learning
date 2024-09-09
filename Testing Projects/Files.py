
import os, shutil


file_name = "tato.py"
path = f"C:\\Users\\hugop\\OneDrive\\Escritorio\\{file_name}"
second_path = f"C:\\Users\\hugop\\OneDrive\\Imágenes\\{file_name}"

text = "print('Hello World, first time in this computer')"

with open(path, "w") as file:
    file.write(text)


try:
    with open(path) as file:
        text_in_file = file.read()
except FileNotFoundError:
    print("This file doesn't exists")

print(text_in_file)

shutil.copyfile("C:\\Users\\hugop\\OneDrive\\Escritorio\\nano.py", "C:\\Users\\hugop\\OneDrive\\Escritorio\\tato.py")


os.replace(second_path, path)


os.remove(f"C:\\Users\\hugop\\OneDrive\\Imágenes\\{file_name}")