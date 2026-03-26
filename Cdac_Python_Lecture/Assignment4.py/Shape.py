from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class circle(Shape):

    def __init__(self,radius):
        self.radius = radius    

    def area(self,radius):
        area= 3.14*radius*radius
        return self.area
    

    









