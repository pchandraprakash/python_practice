"""
Exercise 1.7 – Rock, Paper, Scissors

In this exercise, you are going to practice using conditionals (if, elif, else). You will write a small program that will
determine the result of a rock, paper, scissors game, given Player 1 and Player 2’s choices. Your program will print
out the result. Here are the rules of the game:

1. First create a truth table for all the possible choices for player 1 and 2, and the outcome of the game. This
will help you figure out how to code the game!

2. Create a new file rps.py that will generate the outcome of the rock, scissors, paper game. The program
should ask the user for input and display the answer as follows:

Player 1? rock
Player 2? scissors
Player 1 wins.

The only valid inputs are rock, paper, and scissors. If the user enters anything else, your program should
output “This is not a valid object selection”. Use the truth table you created to help with creating the
conditions for your if statement(s).
"""


def rps():
    player1 = input("player 1? ").upper()
    player2 = input("player 2? ").upper()

    while player1 != ("ROCK" or "PAPER" or "SCISSORS") and player2 != ("ROCK" or "PAPER" or "SCISSORS"):
        print("This is not a valid object selection")
        print("Restart the game")
        exit()

    if player1 == "ROCK" and player2 == "SCISSORS":
        print("ROCK beats SCISSORS. Player 1 has won the match")
    if player1 == "SCISSORS" and player2 == "PAPER":
        print("SCISSORS beats PAPER. Player 1 has won the match")
    if player1 == "PAPER" and player2 == "ROCK":
        print("PAPER beats ROCK. Player 1 has won the match")

    if player1 == "SCISSORS" and player2 == "ROCK":
        print("ROCK beats SCISSORS. Player 2 has won the match")
    if player1 == "PAPER" and player2 == "SCISSORS":
        print("SCISSORS beats PAPER. Player 2 has won the match")
    if player1 == "ROCK" and player2 == "PAPER":
        print("PAPER beats ROCK. Player 2 has won the match")

    while (player1 == "ROCK" and player2 == "ROCK") or \
            (player1 == "PAPER" and player2 == "PAPER") or \
            (player1 == "SCISSORS" and player2 == "SCISSORS"):
        print("It's a Tie!")
        print("Restart the game")
        exit()


rps()

