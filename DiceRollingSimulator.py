import random

number = random.randint(1, 6)
roll = 1
name = input("Enter your name: ")
print("Hi!", name, "Welcome to the dice rolling simulation game...")
question1 = input("Would you like to continue the game? [Y/N]")
if question1 == 'N' or question1 == 'n':
    print("Oh Okay!...Better luck next time")
    print("Please restart the game")
    exit()
if question1 == 'Y' or question1 == 'y':
    print(number)
question2 = input("Would you like to roll the dice again? [Y/N]")
if question2 == 'N' or question2 == 'n':
    print("Oh Okay!...Better luck next time")
    print("Please restart the game")
    exit()
while question1 == 'Y' or question1 == 'y':
    input("Roll the dice again")
    roll += 1
    print(random.randint(1, 6))
    if roll > 6:
        print("You have achieved maximum limit")
        print("Please restart the game")
        exit()
