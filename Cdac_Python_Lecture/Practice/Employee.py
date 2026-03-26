class Employee():
    def __init__(self,id,name):
        self.id = id
        self.name= name

    def display(self):
        print(f"ID:{self.id},Name:{self.name}")

class Manager(Employee):
    def __init__(self,id,name,bonus):
        super().__init__(id,name)
        self.bonus = bonus

    def display(self):
        super().display()
        print(f"Bonus:{self.bonus}")

class Developer(Employee):
    def __init__(self,id,name,Programming_language):
        super().__init__(id,name)
        self.Programming_language = Programming_language
def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")

m = Manager(101, "Ronak", 50000)
d = Developer(102, "Amit", "Python")

print("Manager Details:")
m.display()

print("\nDeveloper Details:")
d.display()