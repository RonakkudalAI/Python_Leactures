class Laptop:
    storage_type ="ssd"

    def __init__(self, Ram, Storage):
        self.Ram = Ram
        self.Storage = Storage
    @classmethod
    def get_storage_type(cls): #Class Methods 
        print(f"Storage_type = {cls.storage_type}")


    def get_info(self): #instance Method
            print(f"Ram of Laptop is{self.Ram} Ram & Storage is {self.Storage}")

    @staticmethod
    def cal_discount(price,discount):
         final_price = price-(discount*price/100)
         print(f"Discounted price ={final_price}")


l1 = Laptop("16gb","512gb")
l1.cal_discount(40_000,10)

l1.get_storage_type()
