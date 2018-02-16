"""
In this exercise, we will ask the user for his/her first and last name, and
date of birth, and print them out formatted.

Output:
Enter your first name: Chuck
Enter your last name: Norris
Enter your date of birth:
Month? March
Day? 10
Year? 1940
Chuck Norris was born on March 10, 1940.
"""

def userinput():
    fn = input("Please enter your first name: ")
    ln = input("Please enter your last name: ")
    print("Please enter your date of birth details")
    month = input("Month?: ")
    day = input("Day?: ")
    year = input("Year?: ")
    print("----------------")
    print(fn, ln, 'was born on', month, day + ',', year)
    exit()

userinput()

