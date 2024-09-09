from animal import Animal, Rabbit, Fish, Hawk

# Main class
animal = Animal()


# Sub-classes
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#
print(rabbit.eat())
print(rabbit.sleep())
print(rabbit.run())


print(fish.eat())
print(fish.sleep())
print(fish.swim())


print(hawk.eat())
print(hawk.sleep())
print(hawk.fly())