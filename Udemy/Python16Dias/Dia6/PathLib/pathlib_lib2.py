# Ctrl + Space -> Search methods, classes, etc...

from pathlib import Path, PureWindowsPath

# PureWindowsPath -> Transform any Path to a windows path

carpeta = Path("C:/Users/hugop/OneDrive/Escritorio/Software_Learning/Udemy/Python16Dias/Dia6/prueba.txt")

# Pure Windows Path
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

# Read method text
print(carpeta.read_text() + "\n")

# Archive name
print("Archive name: " + carpeta.name)
# Suffix name 
print("Suffix name: " + carpeta.suffix)
# Nombre without suffix
print("Stem name: " + carpeta.stem)


# Boolean Return
if not carpeta.exists():
    print("This archive doesn't exist")
else:
    print("It exists")