class Student:
    def __init(self,marks):
        self.marks = marks
        self.setMarks = marks    
    def setMarks(self,m):
        if m > 0 & m <=100:
            self.setMarks = m
        else:
            print("Invalid Marks: ")

    def getGrade(self):
        if self.marks >=80:
            return("Grade - A")
        elif self.marks >=60:
            return("Grade-B")
        elif self.marks >=40:
            return("Grade - C")
        else:
            return("Invalid marks")
      
s1 = Student(75)
print("You get",s1.getGrade())