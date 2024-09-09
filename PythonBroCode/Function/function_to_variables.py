def hello():
    print("Hello")

# Print the location in memory of the function
print(hello)

# Assign the function to a variable (without parentheses)
# Both have the same position in memory
hi = hello
print(hi)
hi()

# Example with print
say = print
say("Whoaaaaaao! This actually works!")


# Example with range

array = range
food = "pizza"

for i in array(1, 54):
    print(i)


