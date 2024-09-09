# +++++++++Format Method+++++++++
# String Format
# str,format()=   optional method that gives users
#                  more contron when displaying output


animal = "cow"
item = "moon"


# .format Arguments

print("The " +animal+ " jumped over the " +item)
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {1}".format(animal, item)) # Positional Argument
print("The {animal} jumped over the {animal}".format(animal="cow", item="moon")) #keyword Argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

print("\n")

# Format Padding

name = "Hugo"

print("Hello, my name is {}. Nice to meet you.".format(name))
print("Hello, my name is {:10}. Nice to meet you.".format(name))
print("Hello, my name is {:<10}. Nice to meet you.".format(name))
print("Hello, my name is {:>10}. Nice to meet you.".format(name))
print("Hello, my name is {:^10}. Nice to meet you.".format(name))
print("Hello, my name is {name:^10}. Nice to meet you.".format(name="Bro"))
print("Hello, my name is {0:^10}. Nice to meet you.".format(name))

print("\n")

# Format Numbers

number = 3.14159
number_two = 1000

print("The number pi is {:.3f}".format(number)) # Numbers after the dot, also round it
print("The number pi is {:,}".format(number_two)) # Put a (,) to all thousand places
print("The number pi is {:b}".format(number_two)) # Convert the number into binary
print("The number pi is {:o}".format(number_two)) # Convert number in octal
print("The number pi is {:X}".format(number_two)) # Convert number in hexadecimal (upper & lower)
print("The number pi is {:x}".format(number_two))
print("The number pi is {:E}".format(number_two)) # Convert the number in Scientific Notation (upper & lower)
print("The number pi is {:e}".format(number_two))
