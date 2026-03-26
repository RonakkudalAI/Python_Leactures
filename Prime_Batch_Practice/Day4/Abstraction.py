#Abstraction
'''
Hiding internal Details and showing only essential features
It has abstract classes
Abstract classes are blueprint for other classes

'''
from abc import ABC

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass
class Lion(Animal):
    def make_sound(self):
        print("Roar")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()