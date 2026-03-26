class Car_Management:

    def __init__(self, speed, name):
        self.speed = speed
        self.name = name

    def accelerate(self, amount):
        self.speed += amount
        print(self.name, "speed increased to", self.speed)

    def show_speed(self):
        print(self.name, "current speed is", self.speed)

    def brake(self, amount):
        self.speed -= amount
        print(self.name, "speed decreased to", self.speed)


# Creating object
car1 = Car_Management(50, "BMW")

car1.accelerate(20)
car1.brake(10)
car1.show_speed() 