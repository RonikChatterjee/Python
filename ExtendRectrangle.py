#   Question3:  Extend the Rectangle class from Question 2 to include a method named display_info. This method should print a message displaying the length, width, and area of the rectangle. Create an object of the class, set the length and width attributes, and then call the display_info method to showcase the information.

import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    def display_info(self):
        print("Length: ", self.length)
        print("Width: ", self.width)
        print("Area: ", self.calculate_area())

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

rectangle = Rectangle(length, width)

rectangle.display_info()