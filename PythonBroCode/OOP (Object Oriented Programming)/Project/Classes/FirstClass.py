class Organism:
    alive = True

    def __init__(self, age):
        self.age = age

    def eat(self):
        print("The organism is eating...")

    def sleep(self):
        print("The organism is sleeping...")


class Animal(Organism):

    def __init__(self, age, legs, arms):
        # Inherit a contructor method
        super().__init__(age)
        self.legs = legs
        self.arms = arms

    def eat(self):
        print("The animal is eating...")

    def sleep(self):
        print("The animal is sleeping...")

    def breathe(self):
        print("The animal is breathing...")


class TerrestrialAnimal(Animal):

    def __init__(self, age, legs, arms):
        super().__init__(age, legs, arms)

    def eat(self):
        print("The terrestrial animal is eating...")

    def sleep(self):
        print("The terrestrial animal is sleeping...")

    def breathe(self):
        print("The terrestrial animal is breathing...")

    def run(self):
        print("The terrestrial Animal is running...")

