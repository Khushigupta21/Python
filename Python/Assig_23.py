# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 

import math

class Circle:
    def __init__(self, radius):
        """
        Constructor method to initialize the Circle object with a radius.
        """
        self.radius = radius

    def compute_area(self):
        """
        Method to compute the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def compute_perimeter(self):
        """
        Method to compute the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius

# Example usage
circle = Circle(5)  # Create an instance of Circle with radius 5
area = circle.compute_area()  # Compute the area of the circle
perimeter = circle.compute_perimeter()  # Compute the perimeter of the circle

print(f"The area of the circle is: {area:.2f}")  # Output: The area of the circle is: 78.54
print(f"The perimeter of the circle is: {perimeter:.2f}")  # Output: The perimeter of the circle is: 31.42
