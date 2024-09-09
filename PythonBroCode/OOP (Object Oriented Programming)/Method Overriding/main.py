class Animal:
    def eat(self):
        print("This animal is eating...")


class Rabbit(Animal):

     # This method 'override' the Animal method
     # It can be define better an exclusively for the class
    def eat(self):
        print("This rabbit is eating...")



rabbit = Rabbit()
rabbit.eat()