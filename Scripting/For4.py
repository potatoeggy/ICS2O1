# Daniel Chen
# Write a program that prompts the user to enter a word and your program should output each letter of the word on a separate line.
# 22 March 2019

word = input('Word: ')
for x in range(len(word)):
    print(word[x])