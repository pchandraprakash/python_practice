"""
3 steps to create a an object in Python:
step 1: write "class" Keyword
step 2: write "class_name" - class name should follow a CamelCase convention.
step 3: parameter for the class name MUST BE "object"

syntax:

class Sample(object):
    print(" This is my first class ")

How to create an Instance of a class?

x = Sample() --> now x is the new instance of the Sample class

A function defined inside a class is known as a Method.
"""


class Sample(object):
    print("This is my first class object")
    print("Sum of 2 numbers: ", 5 + 5)

    def __init__(self, breed):
        self.breed = breed


x = Sample('Husky')
print(x.breed)


class AOT(object):
    polygon = "This program will print the area of triangle..."

    def __init__(self, base, height):
        self.base = base
        self.height = height
        area = (1/2) * self.base * self.height
        print("The area of triangle is", area)
        print("Accessing Class Object Variable through CLASS NAME inside a method: ", AOT.polygon)
        print("Accessing Class Object Variable through SELF inside a method: ", self.polygon)

    print("Accessing Class Object Variable directly inside the class: ", polygon)


triangle = AOT(int(input("Enter the base of the triangle: ")), int(input("Enter the height of the triangle: ")))

"""
The use of SELF while initiating methods is to specify which variable are we accessing, whether is a global variable
or a local variable. Usually global variables are called Class Object Attributes and can be directly accessed without 
SELF.
"""
