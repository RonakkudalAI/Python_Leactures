class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand}{self.model} is starting.......")
    
    def stop(self):
        print(f"{self.brand}{self.model} is stoping........")

class Car(Vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type = fuel_type

    def display(self):
        print("car class Information: ")
        print(f"Brand :{self.brand}")
        print(f"Model : {self.model}")
        print(f"Fuel type :{self.fuel_type}")

c1 = Car("Hyndai","Creta","Electric")
c1.start()
c1.display()
c1.stop()