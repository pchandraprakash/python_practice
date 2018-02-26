class Employee(object):
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' + lname + '@company.com'
        emp = []
        emp.append(self.fname)
        emp.append(self.lname)
        emp.append(self.salary)
        print(self.email)
        print(emp)

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)


n = 0
while n < 1:
    n = n+1
    e = Employee(
        str(input("Enter Employee First Name: ")),
        str(input("Enter Employee Last Name: ")),
        int(input("Enter Salary of the employee: ")))
    e.fullname()


""" Inheritance Example"""


class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Pets(Dog):
    def description(self):
        print("{} is {} years old".format(self.name, self.age))


n = 1
z = int(input("How many dogs do you have? "))
while n < (z+1):
    n = n+1
    p = Pets(str(input("Enter Dog's name: ")), str(input("Enter Dog's age: ")))
    p.description()
print("They are all mammals of course!!!")

""" Class Object Variable and Instance Variable """


class C1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check(self):
        return'{} and {} the variables'.format(self.x, self.y)


class C2(C1):
    def add(self):
        s = self.x + self.y
        print(s)


c2 = C2(2, 3)
c1 = C1(5, 6)
c2.add()
c1.check()




