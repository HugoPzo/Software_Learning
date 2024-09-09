# User Input
# 4

name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = str(input("How tall are you?: "))


print("Hello {} with {} years and your height is {} cm tall".format(name.capitalize(), age, height.replace(".", "")))