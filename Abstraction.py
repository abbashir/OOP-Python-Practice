from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def area(self):
        print("Area = ", .5 * self.dim1 * self.dim2)


class Rectangle(Shape):
    def area(self):
        print("Area = ", self.dim1 * self.dim2)


t = Triangle(20, 30)
t.area()
r = Rectangle(20, 30)
r.area()
