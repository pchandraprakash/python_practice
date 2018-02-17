import random
"""
1. Write a list comprehension that prints a list of the cubes of the numbers 1 through 10.
"""
x = range(1, 11)
"""for elements in x:
    print(elements ** 3) """
cube = [elements ** 3 for elements in x]
print(cube)

"""
2. Write a list comprehension that prints out the possible results of two coin flips (one result would be ’ht’).
(Hint - how many results should there be?)
"""
flip_values = {1: 'ht', 2: 'th', 3: 'tt', 4: 'hh'}
"""for elements in flip_values:
    print(flip_values[random.randint(1, 4)])"""
flip = [flip_values[random.randint(1, 4)] for flip in flip_values]
print(flip)

"""
3. Write a function that takes in a string and uses a list comprehension to return all the vowels in the string.
"""


def lc_vowel():
    string = input("Enter a word: ")
    a = [word for word in string]
    for components in a:
        if components == 'a' or components == 'e' or components == 'i' or components == 'o' or components == 'u':
            print(components)
    else:
        print(string, ": this word does not contain any vowels")


lc_vowel()

"""
4. Run this list comprehension in your prompt:
[x+y for x in [10,20,30] for y in [1,2,3]]
Figure out what is going on here, and write a nested for loop that gives you the same result. Make sure what
is going on makes sense to you!
"""
test = [x+y for x in [10, 20, 30] for y in [1, 2, 3]]
print(test)
"""
Understanding:
take an element from list x and add it to every element of the list y and create a new list
"""
l1 = [10, 20, 30]
l2 = [1, 2, 3]
l3 = []
for elements_list1 in l1:
    for elements_list2 in l2:
        l3.append(elements_list1 + elements_list2)
print(l3)
