# +++++++++Functions+++++++++

"""# A Block of code which is executed
only when it is called"""

# What is inside the '()' is called an argument
def hello(name):
    print(f"Hello {name}")
    print("Have a nice day")


hello("Hugo")


def hi(first_name, last_name, age):
    print(f"Hello {first_name} {last_name} "
          f"with {age} years old")


hi("Hugo", "Perez", 19)