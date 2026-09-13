# wap in python to create a class triangle with 3 variables side1,side2,side3 . initialize the variables using constructor. it also has variables angle1, angle2, angle3 . create a class equilateral triangle and find the area of the triangle with calarea() function . find the tangent of all the angles using findangle() method (i.e tan of angle 1,2,3). create a class scalene which is child of triangle class, find perimeter of triangle with calperimeter() function. find area of triangle with calarea() function. use the math package for computation. print the area as whole number not decimal.
import math
# Parent class
class Triangle:
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


# Child class for Equilateral Triangle
class Equilateral(Triangle):

    def calarea(self):
        area = (math.sqrt(3) / 4) * self.side1 * self.side1
        return round(area)

    def findangle(self):
        print("tan of angle 1 =", math.tan(math.radians(self.angle1)))
        print("tan of angle 2 =", math.tan(math.radians(self.angle2)))
        print("tan of angle 3 =", math.tan(math.radians(self.angle3)))


# Child class for Scalene Triangle
class Scalene(Triangle):

    def calperimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter

    def calarea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * 
                         (s - self.side2) * (s - self.side3))
        return round(area)


# Creating object of Equilateral Triangle
e = Equilateral(6, 6, 6, 60, 60, 60)

print("Equilateral Triangle")
print("Area =", e.calarea())
e.findangle()


# Creating object of Scalene Triangle
s = Scalene(5, 6, 7, 60, 50, 70)

print("\nScalene Triangle")
print("Perimeter =", s.calperimeter())
print("Area =", s.calarea())