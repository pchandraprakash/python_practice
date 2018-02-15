#!/usr/bin/ebv python3

"""In this game we will compare a number entered by a human in comparision with computer generated number,
if the number matches after certain tries, then human will win else he won't"""

import random
number = random.randint(1, 10)
tries = 1

username = input("Hello, what is your username?")
print("Hello", username + ". Welcome to the number guessing game!")

question = input("Do you want to play this game? [Y/N]")

if (question == 'N') or (question == 'n'):
    print("Oh!..Okay, better luck next time")
    exit()

if (question == 'Y') or (question == 'y'):
    print("You should guess a number between 1 - 10")
    guess = int(input("Guess the number: "))
    if guess > number:
        print("Guess lower number...")
    if guess < number:
        print("Guess higher number...")
while guess != number:
    tries += 1
    guess = int(input("Try guessing again: "))
    if guess < number:
        print("Guess higher number...")
if guess == number:
    print("You are right! you have the game!", "The number was", number, \
          "and it was only", tries, "tries")
    exit()
