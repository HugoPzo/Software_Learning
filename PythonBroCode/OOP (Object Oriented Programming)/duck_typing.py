# Duck typing = concept where the class of an object is
#               less important than the methods/attributes
#               class type is not checked if minimum methods/attributes
#               are present.
#               "If it walks like a duck, and it quacks like a duck
#                then is must be a duck"



class Duck:

    def walk(self):
        print("The duck walks")

    def talk(self):
        print("The duck quacks")


class Chicken:

    def walk(self):
        print("The chicken walks")

    def talk(self):
        print("The chicken clucking")


class Person:

    def catch(self, duck):

        duck.walk()
        duck.talk()
        print("You catch it!!!")


duck = Duck()
chicken = Chicken()
person = Person()

# Both parameters (duck, chicken) works, it is because
# both have the same methods, (also works with same attributes)
# Python check that both are similar, so don't care the class
person.catch(duck)

print("\n")

person.catch(chicken)
