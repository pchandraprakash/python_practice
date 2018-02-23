""" This program calculates Body Mass Index (BMI) and Ponderal Index (PI) of a person """


class BMI(object):
    def __init__(self, name, age, mass, height):
        self.mass = mass
        self.height = height
        self.name = name
        self.age = age

    def bmi_calculator(self):
        body_mass_indicator = round(self.mass / self.height**2)
        print("Hi "+self.name+" your BMI value at the age of "+str(self.age)+" year(s) is "+str(body_mass_indicator) +
              " kg/m^2")

        if body_mass_indicator < 18:
            print("BMI Category: Under Weight")
        elif body_mass_indicator < 25:
            print("BMI Category: Normal")
        elif body_mass_indicator < 30:
            print("BMI Category: Overweight")
        elif body_mass_indicator > 30:
            print("BMI Category: Obese")

    def pi_calculator(self):
        ponderal_index = round(self.mass / self.height**3)
        print("Hi " + self.name + " your BMI value at the age of " + str(self.age) + " year(s) is " + str(
            ponderal_index) +
              " kg/m^3")


bmi = BMI(str(input("Enter your name: ")), int(input("Enter your age ")), int(input("Enter your weight in kg: ")),
          float(input("Enter your height in meters: ")))
bmi.bmi_calculator()
bmi.pi_calculator()
