# +++++++++Kwargs (**kwargs)+++++++++

""" Parameter that will pack all arguments into a dictionary
    useful so that a function can accept a varying amount
    of keyword arguments"""


def hello(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

"""# This code works, but if we add another
argument, it'll return an error"""

hello("Hugo", "Perez")


# We use '**kwargs' for this case
# kwargs = Key word arguments
# We convert into a dictionary the arguments

# Both examples how to use it

def hellokwargs(**kwargs):  #(**) define the dictionary argument
    print(f"Hello {kwargs['first']} {kwargs['last']}")

hellokwargs(last="Perez", first="Hugo")


def hellokwargsloop(**kwargs):  #(**) define the dictionary argument
    for key, value in kwargs.items():
        print(value, end=" ")

print("\n")
# Has to be in order
hellokwargsloop(last="Perez", title="Mr", first="Hugo")
print("\n")
hellokwargsloop(title="Mr.", first="Hugo", middle="Perez", last="Ortiz")