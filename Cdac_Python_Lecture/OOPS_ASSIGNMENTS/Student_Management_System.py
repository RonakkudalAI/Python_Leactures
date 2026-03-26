class Student:
    school_name = "CDAC : AI Learning Academy"

    def __init__(self,student_name,age,course):

        self.student_name = student_name
        self.age = age
        self.course = course

    def display(self):
        print(self.student_name,self.age,self.course,Student.school_name)

    def isAdult(self,age):
        if(self.age > 18 ):
             print("You are audlt :")
        elif(self.age > 13 and self.age<18):
            print("You are teenager :")
        else:
             print("You are Minor :")

s1 = Student("Ronak",24,"AI & ML")
s2 = Student("Manali", 23,"MSC")

s1.display()
s2.display()