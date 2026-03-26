class Student:
    def __init__(self,marks):
        self.__marks = marks
        self.setMarks(marks) 

    def setMarks(self,m):
     if m >= 0 and m <=100:
        self.__marks = m
     else:
        print("Invalid Marks")
    
    def getGrade(self):
       if self.__marks >=80:
          return("A-Grade")
       elif(self.__marks >= 60 and self.__marks<80):
            return("B-Grade")   
       elif(self.__marks >= 40 and self.__marks<60):
            return("C-Grade")   
       else:
            return("Fail")
        
s1 = Student(75)
print("You get",s1.getGrade())
          


          