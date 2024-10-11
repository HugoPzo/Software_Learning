# +++++++++ Scope +++++++++

# The region that a variable is recognized
# A variable is only available from inside the region it is created
# A global and locally scoped versions of a variable can be created


name = "Bro" # Global scope (available inside & outside functions)

def display_name():
    # Also global variables can be declared inside functions
    global lastName
    lastName = "Bro"

    name = "Code"   # Local scope (Available only inside the function)
    print(name) # If I errase the variable inside the function, this will print the global variable


display_name()
print(name)

# Python use this order

# L = Local (Function)
# E = Enclosing (NonLocal)
# G = Global (Module)
# B = Built in (Script)