# Import necessary packages
from abc import ABC, abstractmethod


# Create a base class
class Vehicle(ABC):

    # Abstract method
    # Should be implemented by all sub-classes
    def move(self):
        pass


# Sub classes
class Car(Vehicle):

    def move(self):
        print("I can drive on roads")


class Boat(Vehicle):

    def move(self):
        print("I can sail on water")


class Airplane(Vehicle):

    def move(self):
        print("I can fly in the sky")


class Train(Vehicle):

    def move(self):
        print("I can travel on railway tracks")


# Driver code
car_obj = Car()
car_obj.move()

boat_obj = Boat()
boat_obj.move()

plane_obj = Airplane()
plane_obj.move()

train_obj = Train()
train_obj.move()
