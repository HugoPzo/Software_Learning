# +++++++++Tuple+++++++++

# Collection which is ordered and unchangeable
#   used to group together related data


# Tuple
student = ("Hugo", 19, "male")

# Position 1 in tuple
print(student[1])

# Functions
x = student.count("Hugo")
print(x)

y = student.index("male")
print(y)

print("\n")

for i in student:
    print(i, end=" ")

print("\n")

if "Hugo" in student:
    print("Hugo is Here!!")