# What is used to check whether an object o is an instance of class A? 
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Creating instances
my_dog = Dog()
my_cat = Cat()

# Checking instances
print(isinstance(my_dog, Dog))    # Output: True
print(isinstance(my_dog, Animal)) # Output: True
print(isinstance(my_cat, Dog))    # Output: False
print(isinstance(my_cat, Cat))    # Output: True
print(isinstance(my_cat, Animal)) # Output: True
