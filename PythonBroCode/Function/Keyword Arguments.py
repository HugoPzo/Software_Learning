# +++++++++Keyword Arguments+++++++++

"""# Arguments preceded by an identifier when we pass them to a function
     The order of the argument doesn't matter, unlike positional arguments
     Python knows the names of the arguments that our function receives"""


def hello (first, middle, last):
    print(f"Hello {first} {middle} {last}")

# Positional arguments
hello("Hugo", "Perez", "Ortiz")

# Non Positional (Keyword Arguments)
hello(last="Ortiz", first="Hugo", middle="Perez")