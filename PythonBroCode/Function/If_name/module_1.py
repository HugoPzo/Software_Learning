import module_2


print(__name__)
print(module_2.__name__)
print("\n")

def hello():
    print("hello")


if __name__ == "__main__":
    print("running this module directly")
    hello()
else:
    print("running other module indirectly")

print("\n")


