# Daniel Chen
# Prompt the user for a number and print “good” if the number is less than 5, between 8 & 10 or greater than 33. Otherwise, print “bad”. Use the logical or operator in your if statement.
# 20 March 2019

num = float(input('Number: '))

if num < 5 or 8 < num < 10 or num > 33:
    print('Good')
else:
    print('Bad')