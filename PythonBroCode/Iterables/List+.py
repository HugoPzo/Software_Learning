# +++++++++List+++++++++

# Used to store multiple items in a single variable


food = ["pizza", "hamburguer", "hotdog", "spaguetti"]

print(food)

food[0] = "sushi"

print("\n")

print(food[0])
print(food[1])
print(food[2])
print(food[3])

print("\n")

for i in food:
    print(i)

print("\n")

# Function in lists

food.append("ice cream")
print(food)
print("\n")

food.remove("ice cream")
print(food)
print("\n")

food.pop()
print(food)
print("\n")


# Delete an specific element
del food[0]
print(food)
print("\n")

food.insert(0, "cake")
print(food)
print("\n")

food.sort()
print(food)
print("\n")

s = food.count("cake")
print(s)
print("\n")

mexican_food = ["Tacos", "Enchiladas"]
food.extend(mexican_food)
print(food)
print("\n")

x = food.index("Tacos")
print(x)
print("\n")

food.reverse()
print(food)
print("\n")

second_list = food.copy()
print(second_list)
print("\n")

food.clear()
print(food)
print("\n")

