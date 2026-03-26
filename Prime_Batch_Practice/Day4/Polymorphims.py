#Polymorphims
#Many Forms
#Function OverRiding
#Duck Typing walks like a duck and quaks like a duck

class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):
       print("Designation = Teacher")

t1 = Teacher()
t1.get_designation()

#DuckTyping
acc1 = Accountant()
acc1.get_designation()