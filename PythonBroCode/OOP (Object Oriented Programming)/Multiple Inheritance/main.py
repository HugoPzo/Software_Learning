# Multiple Inheritance = When a child is derived from more than one parent class


class Prey:

    def flee(self):
        print("This animal flees...")


class Predator:
    def hunt(self):
        print("This animal hunts...")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass


# This class inherit both classes
class Fish(Prey, Predator):

    def flee(self):
        print("The fish flees")

    def hunt(self):
        print("The fish hunt")


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


print(rabbit.flee())
print(hawk.hunt())

# Fish has both Classes inheritance
print(fish.flee())
print(fish.hunt())

