# Daniel Chen
# 17 May 2019
# Writea program that prompts the user fora letter of the alphabet. If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the letter is a consonant.

vowels = ['a', 'i', 'u', 'o', 'e']
letter = input('Letter: ')

if letter in vowels:
    print(letter + ' is a vowel.')
elif letter == 'y':
    print(letter + ' is sometimes a vowel and sometimes a consonant.')
else:
    print(letter + ' is a consonant.')