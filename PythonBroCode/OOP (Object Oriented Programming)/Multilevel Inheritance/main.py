# multi-level inheritance = when a derived (child)
# class inherits another derived (child) class

# GrandParent
class Organism:

    alive = True

# Parent
class Animal(Organism):
    def eat(self):
        print("This animal eat...")


# Son
class Dog(Animal):
    def bark(self):
        print("This dog is barking...")


dog = Dog()
# Attribute from GrandParent
print(dog.alive)
# Method from Parent
dog.eat()
# Own Method
dog.bark()