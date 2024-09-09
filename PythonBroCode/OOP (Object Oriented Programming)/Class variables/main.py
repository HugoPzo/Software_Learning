
from car import Car

# At this point the class has by default attribute "wheels = 4"
car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Volkswagen", "Golf", 2016, "blue")

# Both will print the defaul amount of wheels '4'
print(car_1.wheels)
print(car_2.wheels)

# Also it can be change (2 Examples)

# Change the variable for only one object
car_1.wheels = 2
print(car_1.wheels)

# Or, change it from the class, and all the object will have that configuration
Car.wheels = 2
print(car_1)
print(car_2)

