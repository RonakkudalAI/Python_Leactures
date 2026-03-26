from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius


    def area(self,radius):
        area= 3.14*radius*radius
        return self.area

class Rectangle(Shape):
    def __init(self,length,breadth):
        self.length= length
        self.breadth= breadth

    def area(self,length,breadth):
        area = length*breadth
        return self.area
    

c = Circle(5)
c.area()
print(f"Area of Circle is {c.area}")

r = Rectangle(10,20)
r.area()
print(f"Area of Rectangle is {r.area()}")


