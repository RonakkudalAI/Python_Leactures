from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Motorbike(Vehicle):
    def start(self):
        print("Started"
              
              
              
              )

    def stop(self):
        print("Stop")

c = Motorbike()
c.start()
c.stop()