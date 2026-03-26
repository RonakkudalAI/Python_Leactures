from abc import ABC, abstractmethod
class A(ABC):
    @staticmethod
    @abstractmethod
    def m1():
        pass

class B(A):
    @staticmethod
   
    def m1():
        print("m1: child class implementation as class method")
a = B()
a.m1()
B.m1()



'''Abstract class Key Pointers:
ABC Is used to create abstract base class
@abstract method is used to declare abstract method
Abstract class object cannot be created
child class must implement all abstract methods
Abstract class can contains
        -normal base
        -Abstract methods
        -Constructors
        -Abstract class method
        -Abstract static methods
        -Abstract property

Vehicle abstract class,
    -method start()
    -method stop()
child class MotorBike







'''