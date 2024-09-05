# What is Instantiation in terms of OOP terminology? 

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Car make: {self.make}, model: {self.model}"

# Instantiation
my_car = Car(make="Toyota", model="Corolla")  # Creating an instance of Car

# Accessing attributes and methods
print(my_car.display_info())  # Output: Car make: Toyota, model: Corolla
