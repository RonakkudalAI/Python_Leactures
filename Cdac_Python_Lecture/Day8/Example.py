class InsufficientBalanceError(Exception):
    pass

def withdraw(balance,amount):
        if amount > balance:
            raise InsufficientBalanceError("Not Sufficient Balance :")

        return balance-amount
    
try: 
        balance = withdraw(30000,50000)

except InsufficientBalanceError as e:
        print("Custom Exception is defined .......",e)
        
