#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

# Base Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Animal speaks"

# Derived Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the base class
        self.breed = breed

    def speak(self):
        return "Woof!"

# Creating an instance of the derived class
my_dog = Dog(name="Buddy", breed="Golden Retriever")

print(f"My dog's name is {my_dog.name}.")        # Output: My dog's name is Buddy.
print(f"My dog is a {my_dog.breed}.")           # Output: My dog is a Golden Retriever.
print(f"My dog says: {my_dog.speak()}")         # Output: My dog says: Woof!
