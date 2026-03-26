class Student:
    def __init__(self,name):
        self.name = name
    
class Teacher:
    def __init__(self,name):
        self.name = name

    def teach(self,student):
        print(f"{self.name} teaches {student.name}")

s1 = Student("Rani")    
t1 = Teacher("Mona")
t1.teach(s1)   #Assosiation Both Class Exists Independently