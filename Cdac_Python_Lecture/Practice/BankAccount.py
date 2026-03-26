class BankAccount:
    def __init__(self,accountNumber,balance):
        self.__accountNumber = accountNumber
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
        else:
            print("Invalid Amount")
    
        print(f"Amount Deposited {self.__balance}")

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        elif amount < 0:
            print("Invalid Amount")
        else:
            self.__balance -= amount

        print("Amount Withdraw Successfully!!",self.__balance)

    def getbalance(self):
        return self.__balance
    
acc1 = BankAccount("101",100000)
acc2 = BankAccount("102",500000)

acc1.withdraw(500)
acc2.deposit(500)

print("Current Balance of acc1",acc1.getbalance())
print("current Balance of acc2",acc2.getbalance())