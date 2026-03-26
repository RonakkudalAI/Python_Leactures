class Employee:
    def display(self):
        print("Hey I am Employee")

class Manager(Employee):
    def display(self):
        # super().display()   # ✅ call parent method
        print("Hey I am Manager")

class Admin(Manager):
    def display(self):
        super().display()   # ✅ call Manager → Employee
        print("Hey I am Admin")

a = Admin()
a.display()