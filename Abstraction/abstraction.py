from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine starts"

class Bike(Vehicle):
    def start(self):
        return "Bike engine starts"

car = Car()
bike = Bike()
print(car.start())
print(bike.start())