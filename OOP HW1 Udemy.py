"""
Object Oriented Programming¶
Homework Assignment
Problem 1
Fill in the Line class methods to accept coordinate as a pair of tuples and return the slope and distance of the line.
"""


class Line(object):

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        pass

    def distance(self):
        print("Distance between given two points: ", ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2) ** 0.5)
        pass

    def midpoint(self):
        x = (self.coor1[0] + self.coor1[1]) / 2
        y = (self.coor2[0] + self.coor2[1]) / 2
        print("Midpoint between two points: ", (x, y))

    def slope(self):
        print("Slope between given two points: ", (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]))
        pass


coor1 = (3, 2)
coor2 = (8, 10)

li = Line(coor1, coor2)

li.distance()
li.slope()
li.midpoint()

print("************")

"""
Problem 2
Fill in the class
"""


class Cylinder(object):
    pi = 3.14

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius
        pass

    def reset(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        print("Volume of Cylinder: ", (2 * Cylinder.pi * self.radius * self.radius) + (2 * Cylinder.pi * self.radius * self.height))
        pass

    def surface_area(self):
        print("Surface Area of Cylinder: ", Cylinder.pi * self.radius * self.radius * self.height)
        pass


c = Cylinder()

c.reset(4, 5)

c.volume()
c.surface_area()
