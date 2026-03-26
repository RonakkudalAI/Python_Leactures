from abc import ABC,abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self,amount):
        pass
class CCPayment(Payment):
    def pay(self,amount):
        print(f"You paid {amount} using Credit Card")

class UpiPayment(Payment):
    def pay(self,amount):
        print(f"you paid {amount} by Upi    ")
