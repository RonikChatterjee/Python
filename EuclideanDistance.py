#   Question1:	Write a python program that calculates the Euclidean distance between two points in a three-dimensional space using a class and object.
import math

class point3D:
    def __init__(self, x,y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        dz = self.z - other_point.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

a = int(input("Enter the value of x1: "))
b = int(input("Enter the value of y1: "))
c = int(input("Enter the value of z1: "))

point1 = point3D(a,b,c)

a = int(input("Enter the value of x2: "))
b = int(input("Enter the value of y2: "))
c = int(input("Enter the value of z2: "))

point2 = point3D(a,b,c)

print("The Euclidean distance between the two points is: ", point1.distance(point2))