# +++++++++While Loops+++++++++
# Statement that will execute it's block of code,
# as long as it's condition remains true
# 9

# Infinite loop

"""while 1==1:
    print("Help, I'm stuck in a loop.")"""

# Correct Loops

"""name = ""

while len(name) == 0:
    name = input("Enter your name: ")


print("Hello {}".format(name))"""

name_2 = None

while not name_2:
    name_2 = input("Enter your name: ")


print("Hello {}".format(name_2))

print(f"Hello {name_2}")