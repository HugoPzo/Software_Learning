

# # Global archives writable paths **********************
from pathlib import Path

## This is a path -> OTHER FORM TO OPEN PATHS
# Can be read on a (Mac / Linux / etc...)
# Can work without 'C:'
carpeta = Path("/Users/hugop/OneDrive/Escritorio/Software_Learning/Udemy/Python16Dias/Dia6") # / "prueba.txt"

archive = carpeta / "prueba.txt"

my_file = open(archive) 
print(my_file.read())
my_file.close()

