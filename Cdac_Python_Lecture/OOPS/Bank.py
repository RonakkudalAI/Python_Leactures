class Bank:
    Bank = "SBI"
    def __init__(self, Name, Balance):
        self.Name = Name
        self.balance = Balance
    def deposite(self, Amount):
        self.balance = self.balance+Amount
        print("Amount is deposite Successfully :")

    def withdraw(self,Amount):
        if Amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= Amount  
        print("Amount withdraw successfully")

    def showbal(self):
        print(self.Name," ", self.balance)

b1 = Bank("Ronak",10000)
b2 = Bank("Manali",2000000)

b1.deposite(100)
b1.withdraw(200)
b1.showbal()