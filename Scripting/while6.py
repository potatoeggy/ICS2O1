# Daniel Chen
# Ask the user to enter a number.  Output the square of the number.  Continue until the user enters a negative number.
# 26 March 2019

while True:
    num = float(input('Number: '))
    if num < 0:
        break
    print(num ** 2)