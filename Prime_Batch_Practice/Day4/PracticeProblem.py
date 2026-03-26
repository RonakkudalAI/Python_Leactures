class Product:
    count = 0

    def __init__(self, Name,Price):
        self.Name = Name
        self.Price = Price
        Product.count+=1
        self.count


    def get_info(self): #instance method
        print(f"price of {self.Name} is Rs.{self.Price}" )

    @classmethod #classMethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")
    
    @staticmethod #static methods
    def cal_discount(price, discount):
        print(f"Discount price = {price -(price*discount/100)}")





p1 = Product("phone",10_000)
p2 = Product("laptop",50_000)
p3 = Product("Tablet",20_000)

p3.get_info()
Product.get_count()
p3.cal_discount(p3.Price,12)


