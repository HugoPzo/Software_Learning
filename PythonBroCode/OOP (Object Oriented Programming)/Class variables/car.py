class Car:

    # Set as default that class 'Car' has the
    # attribute of 4 wheels
    # Outside of the constructor
    wheels = 4  # class variable

    def __init__(self, make, model, year, color):

        self.make = make # instance variable
        self.year = year # instance variable
        self.model = model # instance variable
        self.color = color # instance variable


# Example usage:
hugo = Hugo()
print(hugo.introduce())
print(hugo.learn("Deep Learning"))
print(hugo.show_skills())
