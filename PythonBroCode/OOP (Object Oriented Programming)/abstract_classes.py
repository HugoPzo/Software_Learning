# Abstract Classes

# Prevents a user from creating an object of tha class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation


# Prevent that the user use this class

# Import the 'abc' (abstract) library
# 'ABC' for the class
# "abstractmethod" for the method

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Must to implemtent all the abstract methods
class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("The car stop")


class Motorcycle(Vehicle):

    def go(self):
        print("You drive the motorcycle")

    def stop(self):
        print("The motorcycle stop")

# To prevent tha user use this class, the class must have an
# abstract method
# "vehicle = Vehicle()"
car = Car()
motorcycle = Motorcycle()


# The 'vehicle.go' will return an error, because it is an abstract method
#vehicle.go()

# Abstract classes compels the users to do their own methods
car.go()
motorcycle.go()