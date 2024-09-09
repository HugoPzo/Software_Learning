# +++++++++Modules+++++++++

# Module = a file containing python code. May contain functions, classes, etc.
#           used with modular programming, which is to separate a program
#           into parts


# Different types to import

# This only import the functions we decide
from messages import hello, bye
hello()
bye()


# Import module and then give a name
import messages as ms
ms.hello()
ms.bye()


# This import all from the Module
from messages import *
hello()
bye()



# To see the documentation of what modules are availabel just
# type:
# It list all the modules, also visit the oficial documentation

help("modules")

