def pig_latin():
    word = input("Enter a word: ").lower()
    first_letter = word[0:1]
    print("first letter of this word is:", first_letter)
    if first_letter != 'a' and first_letter != 'e' and first_letter != 'i' and first_letter != 'o' and first_letter != 'u':
        new_word = word[1:len(word)]
        print("This is not a vowel and hence shifting the first letter to the last position and appending it with 'ay' ", new_word + first_letter + 'ay')
    else:
        print("This is a vowel and hence appending the word with 'hay' ", word + 'hay')


pig_latin()
