# walrus operator :=

# (walrus) = morsa

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression


# happy = True
# print(happy)

# Walrus operator (Assign and use, in one expression)
print(happy := True)


# Example without walrus operator
"""
foods = list()
while True:
    food = input("What food do you like? [q to quit]: ")
    if food == "quit":
        break
    foods.append(food)
"""

# Example with walrus operator

# To add "food" as a variable in the list, we must use '()' parentheses
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)


print(foods)


