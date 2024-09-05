# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 

class Rectangle:
    def __init__(self, length, width):
        """
        Constructor method to initialize the Rectangle object with length and width.
        """
        self.length = length
        self.width = width

    def compute_area(self):
        """
        Method to compute the area of the rectangle.
        """
        return self.length * self.width

# Example usage
rect = Rectangle(5, 3)  # Create an instance of Rectangle with length 5 and width 3
area = rect.compute_area()  # Compute the area of the rectangle
print(f"The area of the rectangle is: {area}")  # Output: The area of the rectangle is: 15
