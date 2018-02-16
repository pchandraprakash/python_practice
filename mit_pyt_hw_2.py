"""
1. Write a method rand divis 3 that takes no parameters, generates and prints a random number, and finally
returns True if the randomly generated number is divisible by 3, and False otherwise.
"""

import random

a = random.randint(1, 100)


def rand_divis_3():
    if a % 3 == 0:
        print(True, a)
    else:
        print(False)


rand_divis_3()

print("********")

ds = int(input("Enter the number of sides of the die: "))
dr = int(input("Enter the number of dice to roll: "))


def roll_dice():
    print("dice side: ", ds)
    print("dice roll: ", dr)

    for r in range(1, dr+1):
        print(random.randint(1, ds))


roll_dice()

