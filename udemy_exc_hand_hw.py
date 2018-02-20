"""
Problem 1
Handle the exception thrown by the code below by using try and except blocks.
"""
try:
    for i in ['a','b','c']:
        print(i**2)
except Exception:
    print("There is a problem with your code. Please fix it")
"""
Problem 2
Handle the exception thrown by the code below by using try and except blocks. 
Then use a finally block to print 'All Done'.
"""
try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print("You cannot divide a number by 0. Please fix the issue")
finally:
    print("All Done!")
"""
Problem 3
Write a function that asks for an integer and prints the square of it. Use a while loop with a try,except, 
else block to account for incorrect inputs.
"""


def ask():
    while True:
        try:
            x = int(input("Input an integer: "))
        except Exception:
            print("An error occurred! Please try again!")
        else:
            print("Thank you. The square of your number is:", x**2)
            break
    pass


ask()
