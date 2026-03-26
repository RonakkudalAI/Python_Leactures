class BankAccount:
    def __init__(self,accountNumber,balance):
        self.__accountNumber = accountNumber
        self.__balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Account Number : {self.__accountNumber}: Deposited {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if(amount <= 0):
            print("Invalid amount")
        elif(amount > self.__balance):   
            print("Insuffcient Balance")
        else:
            self.__balance -= amount
            print(f"Account {self.__accountNumber}: Withdrawn {amount}")

    def getBalance(self):
        return self.__balance
    
acc1 = BankAccount(101,200000)
acc2 = BankAccount(102,300000)

acc1.withdraw(1000)
acc2.deposit(1000)
print("Current Balance :" ,acc1.getBalance())
print("Current Balance :",acc2.getBalance())

