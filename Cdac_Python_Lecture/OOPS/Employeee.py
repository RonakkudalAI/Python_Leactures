class Emoployee:
    Company = "IBM"

    def __init__(self, Name,sal):
        self.Name = Name
        self.sal = sal

    def display(self):
        print(self.Name," ", self.sal, " ", Emoployee.Company)

E1 = Emoployee("Ronak",5000)
E1.display()