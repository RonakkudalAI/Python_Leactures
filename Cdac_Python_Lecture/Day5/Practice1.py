# We have two parent admin , manager

class Admin():
    def __init__(self):
         print("Amdin Constructor")
    def display(self):
         print("Hey i am Admin")
class Manager():
     def __init(self):
          super().__init__()
          print("Manager Constructor")
     def display(self):
          print("Hey i am Manager")

          
class Employee(Admin,Manager):
     def display(self):
        print("I am Employee")

E = Employee()
E.display()
print(Employee.mro())