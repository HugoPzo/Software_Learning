# List comprehension = a way to create a new list with less syntax
                        # can mimic certain lambda functions, easier to read
                        # list = [expression for item in iterable]
                        # list = [expression for item in iterable if conditional]
                        # list = [expression if/else for item in iterable]

# Example

grades = [3, 6, 2, 10, 5, 8, 3, 6, 4]
[print(i, end=" ") for i in grades]
print("\n")

# Both works the same

squares = []

# 3 lines
for i in range(1, 11):
    squares.append(i*i)
print(squares)

# 2 lines
squares = [i*i for i in range(1, 11)]
print(squares)
print("\n")

# Mimic certain lamda functions

students = [100, 90, 70, 60, 50, 30, 20, 10]
passed_students = list(filter(lambda x:x >= 60, students))
print(passed_students)


passed_students = [i for i in passed_students if i >= 60]
print(passed_students)

passed_students = [i if i >= 60 else "Failed" for i in students]
print(passed_students)

passed_students = ["Aprooved" if i >= 60 else "Failed" for i in students]
print(passed_students)
