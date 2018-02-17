"""
Write a function roots that computes the roots of a quadratic equation. Check for complex roots and print an
error message saying that the roots are complex.
Hint 1: Your function should take three parameters- what are they?
Hint 2: We know the roots are complex when what condition about the discriminant is met?
Be sure to use a variety of test cases, that include complex roots, real roots, and double roots
"""

a = int(input("value of a: "))
b = int(input("value of b: "))
c = int(input("value of c: "))


def roots():
    z1 = (-b + (b**2 - 4*a*c)**0.5) / 2*a
    z2 = (-b - (b**2 - 4*a*c)**0.5) / 2*a
    print("Roots of the equation are: ", z1, z2)


roots()

