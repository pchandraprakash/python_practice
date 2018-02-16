"""
1. Using a for loop, write a program that prints out the decimal equivalents of 1/2, 1/3, 1/4, . . . , 1/10.
"""
n = list(range(1, 11))
for decimal_equivalent in n:
    print(1/decimal_equivalent)


print("***********************")
print("***********************")
print("***********************")

"""
2. Write a program using a while loop that asks the user for a number, and prints a countdown from that number
to zero. What should your program do if the user inputs a negative number? As a programmer, you should
always consider “edge conditions” like these when you program! (Another way to put it- always assume the
users of your program will be trying to find a way to break it! If you don’t include a condition that catches
negative numbers, what will your program do?)
"""
num = int(input("Enter an integer: "))
x = num > 0
if num > 0:
    while x is True:
        num = num - 1
        print(num)
        if num == 0:
            break
else:
    print("Number should be positive")
    print("Re-enter the number again")


print("***********************")
print("***********************")
print("***********************")

"""
3. Write a program using a for loop that calculates exponentials. Your program should ask the user for a base
base and an exponent exp, and calculate base exp.
"""
base = int(input("Base? "))
exponent = int(input("Exponent? "))
series = " "
for b_e in series:
    print("Exponential Value:", base**exponent)


print("***********************")
print("***********************")
print("***********************")

"""
4. Write a program using a while loop that asks the user to enter a number that is divisible by 2. Give the user
a witty message if they enter something that is not divisible by 2- and make them enter a new number. Don’t
let them stop until they enter an even number! Print a congratulatory message when they *finally* get it
right.
"""
number = int(input("Enter a number: "))
while number % 2 != 0:
    print(number, "Oh :-P, I think you haven't understood the requirement properly, please check the specs again.")
    number = int(input("Enter correct number: "))
    while number % 2 == 0:
        print(number, "Finally, you got it right...Congrats")
        exit()
if number % 2 == 0:
    print(number, "Great, you got it right in first attempt...Many Congratulations")
    exit()
