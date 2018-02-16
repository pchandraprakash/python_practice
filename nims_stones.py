"""
In this game, two players sit in front of a pile of 100 stones. They take turns, each removing between 1 and 5 stones
(assuming there are at least 5 stones left in the pile). The person who removes the last stone(s) wins.

In this problem, you’ll write a function to play this game; we’ve outlined it for you. It may seem tricky, so break
it down into parts. Like many programs, we have to use nested loops (one loop inside another). In the outermost
loop, we want to keep playing until we are out of stones. Inside that, we want to keep alternating players. You have
the option of either writing two blocks of code, or keeping a variable that tracks the current player. The second
way could be slightly trickier, but it’s definitely do-able!
Finally, we might want to have an innermost loop that checks if the user’s input is valid. Is it a number? Is it a
valid number (e.g. between 1 and 5)? Are there enough stones in the pile to take off this many? If any of these
answers are no, we should tell the user and re-ask them the question.
"""

pile = 100
while pile != 0:
    player_a = int(input("player A, choose a value between 1 and 5: "))
    while player_a > 5:
        player_a = int(input("please correctly, choose a value between 1 and 5: "))
    print("player A selected,", player_a)

    pile = pile - player_a
    print("new pile value is,", pile)

    if pile < 0:
        print("No more stones left in the pile. Restart the game")
        exit()

    player_b = int(input("player B, choose a value between 1 and 5: "))
    while player_b > 5:
        player_b = int(input("please correctly, choose a value between 1 and 5: "))
    print("player B selected,", player_b)

    pile = pile - player_b
    print("new pile value is,", pile)

    if pile < 0:
        print("No more stones left in the pile. Restart the game")
        exit()
