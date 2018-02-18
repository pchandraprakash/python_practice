"""
Exercise 3.1 – Additional List Practice

Write a function list intersection
that takes two lists as parameters. Return a list that gives the intersection of the two lists- ie, a list of elements that
are common to both lists. Run the following test cases and make sure your results are the same (nb: the ordering
of your outputs does not matter - [3,2] is the same as [2,3]):
"""
l3 = []


def list_intersection(l1=list(input("Enter list 1: ").split(',')), l2=list(input("Enter list 2: ").split(','))):
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                l3.append(int(e1))
    print(l3)


list_intersection()
print("*********************************************************************")
"""
Exercise 3.2 – Collision Detection of Balls

write a function ball collide that takes two balls as parameters and computes if they are
colliding; your function should return a Boolean saying whether or not the balls are colliding. 
"""


def ball_collide():
    print("Enter the circle properties as per the syntax (x,y,r)")
    print("Where (x,y) defines the center of the circle and 'r' is the radius")
    print("=====================================================================")
    circle_1 = tuple(input("values of x1, y1 and r1 for circle_1? ").split(','))
    circle_2 = tuple(input("values of x2, y2 and r2 for circle_2? ").split(','))
    (x1, y1, r1) = circle_1
    (x2, y2, r2) = circle_2
    distance = round(((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2) ** 0.5)
    radius = (int(r1) + int(r2))
    print("Distance value: ", distance)
    print("Radius value: ", radius)
    if distance <= radius:
        print(2 == 2)
    else:
        print(2 == 1)


ball_collide()
print("*********************************************************************")
"""
Exercise 3.3 – An Introduction to Dictionaries
Explains the following operations that can be performed on Dictionaries

d1 = {}  # an empty dictionary
d2 = {'key_1': 'value_1'}  # create a non-empty dictionary
d2['key_1'] # returns the value that's mapped to the key. If the key doesn't match then you might get the value
d2['key_1'] = 'new_value'  # existing value associated with the key will be changed/overridden by this new value and this can be any python data structure.
del d2['key_1'] # delete the mapping with that key from dictionary d2
len(d2)  # returns the number of entries(mappings) in the dictionary
x in d2 or x not in d2 # checks whether x is in the dictionary d2 or not
d2.keys() # returns a list of all the keys in the dictionary
d2.values() - returns a list of all the values in the dictionary.


Practice:
dictionary = {'k1': 123, 'k2': 'abc', 'k3': 1.234}
print(dictionary['k1'])
dictionary['k1'] = 234
print(dictionary['k1'])
del dictionary['k3']
print(len(dictionary))
print('k1' in dictionary)
print(dictionary.keys())
print(dictionary.values())
"""
class_dictionary = {'1': ('ITMD 510  Object Oriented Application Development',
                          'ITMD 523  Advanced Database Management',
                          'ITMD 574  Information Technology Management Frameworks'),
                    '2': ('ITMD 566  Service-Oriented Architectures',
                          'ITMD 521	Client Server Technologies & Applications',
                          'ITMD 525	Topics in Data Science and Management',),
                    '3': ('ITMD 526	Data Warehousing',
                          'ITMD 527	Data Analytics',
                          'ITMM 586  Information Technology Auditing'),
                    '4': 'ITMM 572  Process Engineering for Information Technology Managers'
                    }

print("Please Note: If you have more one subject then follow this syntax: ('sub1, 'sub2', 'sub3') ")


def add_class(class_num=(input("Enter new class number: ")), desc=input("Enter new class name(s): ")):
        class_dictionary.update({str(class_num): str(desc)})
        print_class()


def print_class(key=(input("class number? "))):
            print(class_dictionary[str(key)])
            print(class_dictionary)


add_class()
