# method chaining = calling multiple methods
#                   sequentially each call performs an
#                   action on the same object and returns
#                   self


class Car:

    def turn_on(self):
        print("You start the engine...")
        return self

    def drive(self):
        print("You start the driving...")
        return self


    def brake(self):
        print("You step on the brakes...")
        return self


    def turn_off(self):
        print("You turn off the engine...")
        return self




car = Car()

# We can chain methods, but inside the methods
# must to 'return self" inside the method, instead, will return an error 'NoneType'

# Using 'return self' we go back to the class
car.turn_on().drive()

print("\n")
(car.turn_on().
 drive().
 brake().
 turn_off())