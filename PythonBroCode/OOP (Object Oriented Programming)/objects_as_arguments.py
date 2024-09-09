class Car:

    color = None


class Motorcycle:

    color = None

# "Function" not method
# The parameter 'vehicle' for this function is an Object
# The parameter 'color' is an attribute from the class
def change_color(vehicle, color):

    vehicle.color = color

# Objects
car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

# Assign the object an the attribute color
change_color(car_1, "Red")
change_color(car_2, "Blue")
change_color(car_3, "White")

change_color(bike_1, "Black")


print(car_1.color)
print(car_2.color)
print(car_3.color)


print(bike_1.color)
