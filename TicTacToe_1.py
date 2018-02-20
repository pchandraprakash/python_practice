import random

# The Game Board
board = list(range(0, 9))


# Presenting the game board in a good fashion
def show():
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])


def checkline(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True


def checkall(char):
    # all the horizontal possibilities (3)
    if (checkline(char, 0, 1, 2) or
checkline(char, 3, 4, 5) or
checkline(char, 6, 7, 8) or
checkline(char, 0, 3, 6) or
checkline(char, 1, 4, 7) or
checkline(char, 2, 5, 8) or
checkline(char, 0, 4, 8) or
checkline(char, 2, 4, 6)
):
        return True


print("--- LET'S PLAY TIC-TAC-TOE ---")
# Take the use input through a while loop and this would be our main game loop
while True:
    print("---------------------------")
    show()
    uip = input("User! please select a spot: ")
    """make sure the input is an integer because the list board will accept ONLY integer values"""
    uip = int(uip)

    if (8 - uip) < 0:
        print("Sorry!..No More Slots Available")
        break

    if board[uip] != ('x' or 'X') and board[uip] != ('o' or 'O'):
        board[uip] = 'x'
        print("User finished his turn")
        print("---------------------------")
        # let us put a check condition to check whether user has won the game or not
        if checkall('x' or 'X'):
            print("--- User Has Won The Game ---")
            show()
            break

        # This code will allow opponent to enter his value
    while True:
        random.seed()  # gives a random generator
        opponent = random.randint(0, 8)  # this will generate a random number between 0 & 8

        if board[opponent] != ('o' or 'O') and board[opponent] != ('x' or 'X'):
            board[opponent] = 'o'
            print("Computer has finished its turn")
            print("---------------------------")
            if checkall('o' or 'O'):
                print("--- Computer Has Won The Game ---")
                show()
                break
            break

    else:
        print("This spot has been taken!, please try some other spot")
    show()
