class BankAccount:
    bank_name = "Secure Bank" 
    
    def __init__(self,Name,balance =0):
        self.Name = Name
        self.balance = balance
    # def __init__(self, Name, balance=0):
    # self.Name = Name
    # self.balance = balance

    def deposit(self,amount):
        if(amount > 0):
            self.balance = self.balance + amount 
            print("Amount Deposited ",self.balance)
        else:
            print("Invalid Amount")
    
    def withdraw(self,amount):
        if(amount <= self.balance):
            self.balance = self.balance-amount
            print("Amount Withdraw Successfully:",self.balance)
        else:
            print("Amount is higher then balance:")
    
    def check_balance(self,):
        print(self.Name,BankAccount.bank_name,self.balance)

b1 = BankAccount("Ronak",10000)
b2 = BankAccount("Manali",20000)

b1.deposit(2000)
b2.withdraw(5000)
b1.check_balance()
b2.check_balance()