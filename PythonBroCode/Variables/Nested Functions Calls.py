# +++++++++Nested Functions Calls+++++++++

"""# Function calls inside other function calls
     innermost function calls are resolved first
     returned value is used as argument for the next outer function"""


# If we enter num='-3.14' the program will return 3
# But we can use less lines of code
"""
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)
"""

# Same result in the same line
print(round(abs(float(input("Enter a whole positive number: ")))))