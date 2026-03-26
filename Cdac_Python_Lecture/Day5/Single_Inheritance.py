'''
A Child class ingeris properties and methods from only one parent class.
Child class can access the methods of parent class.
This is the simplest form of inheritance.
'''
class Animal:
    def sound_of_animal(self):
        print("Voice sound")

class Dog(Animal):
    def sound_of_Dog(self):
        print("Bark")
d = Dog()
d.sound_of_Dog()
d.sound_of_animal()

