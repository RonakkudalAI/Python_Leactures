#Inheritance
#Reusing attr and methods from a parents(Base) class.

class Employee:
    start_time ="10am"
    end_time ="6pm"

class Teacher(Employee):#Inheritance
    def __init__(self,  subject):
        self.subject = subject
t1 = Teacher("Maths")

class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role

staff1 = AdminStaff("Manager")

print(staff1.role, staff1.start_time, staff1.end_time)

#print(t1.subject,t1.start_time,t1.end_time)
''''''