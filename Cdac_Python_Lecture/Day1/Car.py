class Engine:
    def __init__(self, engine_no, power):
        self.engine_no = engine_no
        self.power = power

    def start(self):
        print(f"Engine {self.engine_no} with capacity {self.power}")


class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine   # composition

    def start1(self):
        print(f"Brand name = {self.brand} with model = {self.model}")
        self.engine.start()

    def display(self):
        print("Car details...........")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Engine No: {self.engine.engine_no}")
        print(f"Power: {self.engine.power}")


E1 = Engine("ABSBGSHGHW2883738", 150)
C1 = Car("Honda", "City", E1) #Passing Objec of one class to another class Car-Has an Engine

C1.start1()
C1.display()