# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

class Car:
    def __init__(self, make, model, year):
        # Constructor method to initialize attributes
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        # Method to display car information
        print(f"{self.year} {self.make} {self.model}")

    def start_engine(self):
        # Method to simulate starting the engine
        print("The engine is now running.")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Calling methods on the instance
my_car.display_info()  # Output: 2020 Toyota Corolla
my_car.start_engine()  # Output: The engine is now running.
