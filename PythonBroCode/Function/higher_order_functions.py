# Higher Order Function = a function that either:
                        # 1. accepts a function as an argument
                        # or
                        # 2. returns a function
                        # (In python functions are also treated as
                        # objects)


# Number 1
# -----------------------
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

# Pass the funtion as a parameter
def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)


hi = loud
hii = hi
print(hii)
# -----------------------

# Number 2

def divisor(x):
    def dividend(y):
        return y / x
    return dividend


# Once we assign something to
# variable 'x' will stay the same argument assign until we
# change it or finish the program
divide = divisor(2)
print(divide(10))


divide_2 = divisor(3)
divide_3 = divide_2(18)
print(divide_3)