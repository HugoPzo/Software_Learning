# +++++++++Args (*args)+++++++++

# *args = Parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments


def add(num1, num2):
    return num1 + num2


# This code works, but if I try to add another argument
# inside the function will return an error
print(add(2, 4))

print("\n")
# But with *args doesn't work like that

def addargs(*args): # (*) The asterisk define the tuple arguments
    result = 0
    for i in args: # Need a loop for args
        result += i
    return result

# Doesn't matter how many arguments you throw to the function
print(addargs(4, 1, 3, 6, 8, 5))

# Knowing that a tuple can't be modified
# But if we want to modify a valor we can cast it

def addargscast(*args):
    result = 0
    stuff = list(args)
    stuff[0] = 12
    for i in stuff:
        result += i
    return result


print(addargscast(1, 2, 3, 4, 5, 6, 7))