# Import necessary module
from abc import ABC, abstractmethod


# Create base class
class BaseDevice(ABC):

    # Function to display a value
    def display(self, value):
        print("Received value:", value)

    # Abstract method
    @abstractmethod
    def operate(self):
        print("We are inside BaseDevice operate")


# Create sub class
class MobileDevice(BaseDevice):

    def operate(self):
        print("We are inside MobileDevice operate")


# Object of MobileDevice created
mobile = MobileDevice()

mobile.operate()
mobile.display(250)
