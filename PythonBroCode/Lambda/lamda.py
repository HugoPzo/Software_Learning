# lambda = function written in 1 line using 'lamda' keyword
           # accepts any number of arguments, but only has one expression.
           # (think of it as a shortcut)
           # (useful if needed for a short period of time, throw-away)


# ---- Structure
# lambda parameters:expression

# Accept unlimited parameters, but only has one return


# Normal function
"""def double(x):
    return x*2

print(double(10))"""

# Structure
# lambda arguments : expression(return)

# Double the argument
double = lambda x:x * 2
print(double(5), "\n")

# Multiply two arguments
multiply = lambda x,y:x*y
print(multiply(10,2), "\n")

# Sum of 3 arguments
add = lambda x,y,z: x+y+z
print(add(6,2,8), "\n")

# Return the full name, with two arguments
full_name = lambda first_name, last_name: f"{first_name} {last_name}"
print(full_name("Hugo", "Perez"), "\n")

# Check if the age is >= 18
check_age = lambda age:True if age >= 18 else False
print(check_age(22), "\n ")

# List comprehension

number_list = [2, 6, 3, 1, 7]
# for loop in one line, printing all elements
[print(i) for i in number_list]