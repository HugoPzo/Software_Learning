import os

ruta = "C:/Users/hugop/OneDrive/Escritorio/Software_Learning/Udemy/Python16Dias/Dia6"

# Current working directory (cwd) .getcwd()
path = os.getcwd()

print(path)

# Change directory .chdir(path)
os.chdir(path)

# Make a directory .mkdir(path+name_dir)
os.mkdir(path + "\hola")

# Basename (Only the last element)
base_name = os.path.basename(ruta)
print(base_name)

# Dirname (The full name of the directory)
dir_name = os.path.dirname(ruta)
print(dir_name)

# Both elements in a tuple
split_name = os.path.split(ruta)
print(split_name)


# Delete Directories
os.rmdir(path + "/hola")


