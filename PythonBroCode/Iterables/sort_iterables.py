
# sort() method = used with lists
# sort() function = used with iterables
# sorted(argument) = Sort the list or iterable temporarily, also change other iterables into list

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

# Just for lists ------------------------------------------
students.sort()
# Also can use the keyword "reverse=True" if we want to reverse the list
# Example:  students.sort(reverse=True)
[print(i) for i in students]
print("\n")
# ------------------------------------------

# For other iterables

students_tuple = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")
# This function change the tuple, or other iterable into a list sorted
sort_students_tuple = sorted(students_tuple)
[print(j) for j in sort_students_tuple]
print("\n")


# List of iterables

students_tuple = [("Squidward", "B", 22),
                  ("Sandy", "A", 43),
                  ("Patrick", "F", 35),
                  ("Spongebob", "D", 32),
                  ("Mr.Krabs", "C", 65)]

# 1. Order the list by name
students_tuple.sort()
[print(i) for i in students_tuple]
print("\n")
# Print the list sorted, by names, first argument(default)



# 2. Order list by grades
    # Function Object (La funcion es tratada como un objeto, nos retorna ese valor del objeto)
    # Esta accediendo al mismo punto en memoria, por eso es que la funcion se ejecuta, retorna el valor deseado
        # La keyword "key=" ordena la lista por el parametro que especifiquemos, por ejemplo
        # "key=len()" en este caso, ordenaria por el largo, tanto de numero como de string

        # It works like this...
        # key = a function that's going to return something

# grade will be a function object
# In this case, it'll return the index of the specific column that we want
# What matters, is what ir returning our function object
grade = lambda grades:grades[1]
students_tuple.sort(key=grade)
[print(k) for k in students_tuple]
print("\n")
# Reverse
# students_tuple.sort(key=grade, reverse=True)


# 3. Order list by age
# Also works with lamda
def age(tuple):
    return tuple[2]
students_tuple.sort(key=age)
[print(l) for l in students_tuple]
print("\n")


students_tuple_tuple = (("Squidward", "B", 22),
                  ("Sandy", "A", 43),
                  ("Patrick", "F", 35),
                  ("Spongebob", "D", 32),
                  ("Mr.Krabs", "C", 65))

# We change the tuple of tuple into a list
# Works the same as the last example
tuple_sort = sorted(students_tuple_tuple, key=grade)
"""
tuple_sort = sorted(students_tuple_tuple, key=age)
tuple_sort = sorted(students_tuple_tuple)
"""
[print(m) for m in tuple_sort]

