
# Main Class
class Animal:

    # class 'Animal' is the main class

    alive = True

    def eat(self):
        print("This animal is eating...")

    def sleep(self):
        print("This animal is sleeping...")


# Sub-Class

# All these sub-classes inherit from class 'Animal'
# That mean that they inherit all the (methods / attributes)
# from the main class.

class Rabbit(Animal):

    # The sub-classes can have their own methods & attributes
    def run(self):
        print("The rabbit is running...")


class Fish(Animal):

    def swim(self):
        print("The fish is swimming...")


class Hawk(Animal):

    def fly(self):
        print("The hawk is flying...")



