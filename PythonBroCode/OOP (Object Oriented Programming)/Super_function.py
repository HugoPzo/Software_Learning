# super() = Function used to give access to the attributes of a parent
#           class
#           Returns a temporary object of a parent class when used


# We call it like this inside the own constructor
#   super().___init__(attributes wanted from the parent):

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        # This is the super function.
        # Just define the attributes in the parent class
        # Not necessary to repeat the code
        super().__init__(length, width)


    def area(self):
        return self.length * self.width


class Cube(Rectangle):
    # In this case ´height´ is a attribute only for Cube, but
    # it is using both parents attributes
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height


    def volume(self):
        return self.width*self.height*self.length



square = Square(3, 6)
cube = Cube(4, 5, 3)


print(square.area())
print(cube.volume())