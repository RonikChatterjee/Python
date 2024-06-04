#   Question2:  Create a Python class named Rectangle to represent rectangles. The class should have the following attributes: length and width. It should also have a method named calculate_area that calculates and returns the area of the rectangle. Create an object of the class and demonstrate the calculation of the area.
import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

rectangle = Rectangle(length, width)

print("The area of the rectangle is: ", rectangle.calculate_area())