# +++++++++Return Statement+++++++++

# Functions send Python Values/objects back to the caller.
#               These values/objects are known as the function's return value


def multiply(number1, number2):
    result = number1 * number2
    return result


print(multiply(5, 1))

x = multiply(5, 3)
print(x)


# Also we can use less lines of code

def multiply2(number1, number2):
    return number1*number2


print(multiply2(4, 12))

y = multiply2(8, 3)
print(y)
