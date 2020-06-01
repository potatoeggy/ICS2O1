# Daniel Chen
# Write a program that asks the user for their name and a number and print the name on the screen.  Continue to ask for their name until they enter a negative number.
# 26 March 2019

while True:
    name = input('Name: ')
    num = int(input('Number: '))
    if num < 0:
        break
    else:
        print(name)