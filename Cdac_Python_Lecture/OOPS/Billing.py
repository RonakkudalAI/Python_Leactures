#you have to create a bill with 18 gst and you have to print amount to the given billing
#cal_billing
# Take price in input 

class Bill:
    tax = 0.18
    def __init__(self):
        self.price = int(input("Enter the product Price :"))
    def cal_bill(self):
        self.Amount = self.price + (self.price*Bill.tax)
    def display(self):
        print("Total Billing Amount is : ",self.Amount)
B = Bill()
B.cal_bill()
B.display()

