# Create class
class Car:

    # Create init method
    def __init__(self, top_speed, fuel_mileage):

        # Bind the arguments
        self.top_speed = top_speed
        self.fuel_mileage = fuel_mileage


# Object creation
sedan = Car(220, 20)


# Access the variables inside init method
print("Car Top Speed:", sedan.top_speed)
print("Car Fuel Mileage:", sedan.fuel_mileage)
