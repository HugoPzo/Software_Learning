from pathlib import Path

# Absolute Path to the principal directory of the user
base = Path.home()
print("Absolute Path of User: ")
print(base)
print("\n")

# Path Class -> Create a Path with args
guia = Path("Barcelona", "SagradaFamilia")
print("Create a 'guia' path: ")
print(guia)
print("\n")

# Method 'with_name(str)' -> Change last archive
guia2 = guia.with_name("LaPedrera.txt")
print("Create a 'guia2' path 'with_name': ")
print(guia2)
print("\n")

print("Different types to construct a Path: ")
# Constructor Path admites "strings" & "objects"
# The path above can be in different paths
absolute_path = Path(base, guia, "capilla.txt")
print(absolute_path)

absolute_path = Path(base, Path(guia, "capilla.txt"))
print(absolute_path)
print("\n")

print("Parent Path: ")
# Parent path
print(absolute_path.parent)
print(absolute_path.parent.parent)
print(absolute_path.parent.parent.parent)
print("Parents: ")
print(absolute_path.parents[2])

print("\n\n")

# Enumerate all archives
enum_path = Path(Path.cwd())


print("Same Directory:")
# Only enumerate the archives '.txt' inside the path selected
for txt in enum_path.glob("*.txt"):
    print(txt)


print("\n" + "Directory and Subdirectories: ")
# Enumerate all the archives '.txt' inside the directory and subdirectories
#                               ("**/*.end"")
for txt in enum_path.glob("**/*.txt"):
    print(txt)

print("\n")


# Relative to -> Get a portion of a long path
print("Relatives Path: ")
relativa = Path("Europa", "Espania", "Madrid", "ElPrado.txt")
en_europa = relativa.relative_to(Path("Europa"))
en_espania = relativa.relative_to(Path("Europa", "Espania"))
en_madrid = relativa.relative_to(Path("Europa", "Espania", "Madrid"))


print(en_europa)
print(en_espania)
print(en_madrid)