from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def display(self):
        pass
class Rectangle(Shape):
  
  def area(self):
      print("Area of Rectangle")
    
  def display(self):
    print("This is rectangle !")

r = Rectangle()
r.area()
r.display()