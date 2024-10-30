#  (windows defender may prevent from running)
#  (make sure pip and pyinstaller are installed/updated)

# cd to directory that contains '.py' file
# Command Structure

# PyInstaller  !IMPORTANT

# python -m PyInstaller arguments

# Example : python -m PyInstaller -F -w -i .ico .py

            #   -m          run a module directly

            #   -F          (all in 1 file)
            #   -w          (removes terminal window) (Omitir si se necesita
                                                     # la ventana de la terminal)
            #   -i icon.ico     (adds custom icon to .exe) (Must be ".ico")
            #   file_name.py    (name of main python file)

#   .exe is located in the dist folder  ------ IMPORTANT



# PROBLEM SOLUTION

# The 'typing' package is an obsolete backport of a standard library package and is incompatible with PyInstaller. Please remove this package (located in C:\Users\hugop\AppData\Roaming\Python\Python311\site-packages) using
#     "C:\Program Files\Python311\python.exe" -m pip uninstall typing
# then try again.

# USE
    # pip uninstall typing