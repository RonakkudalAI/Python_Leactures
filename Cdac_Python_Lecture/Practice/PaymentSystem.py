from abc import ABC,abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass
class CCPayment(Payment):
    def pay(self,amount):
        print(f"You paid {amount} by Credit card")

class UPIPayment(Payment):
    def pay(self,amount):
        print(f"You paid {amount} by Upi Method")
p1 = CCPayment()
p1.pay(1000)

p2 = UPIPayment()
p2.pay(500)