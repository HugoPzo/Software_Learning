# Class
class Car:


    # Constructor
    # Special method that create objects for us "__init__(self)"
    def __init__(self, make, model, year, color):
        # Attributes (Is / Has)
        self.make = make
        self.year = year
        self.model = model
        self.color = color


    # Methods (What can do / Or do)

    def drive(self):
        print(f"This {self.model} is driving...")

    def stop(self):
        print(f"This {self.model} is stopped...")