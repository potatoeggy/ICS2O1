# Daniel Chen
# Write a program that prompts the user to enter 3 numbers, and prints the largest value.
# 20 March 2019

x = float(input('Number 1: '))
y = float(input('Number 2: '))
z = float(input('Number 3: '))

'''
if x == y or x == z or y == z: # Handling equals first just in case
    if x == y and x != z:
        if z > x:
            greatest = z
        else:
            greatest = str(x) + ', ' + str(y)
    elif x == z and x != y:
        if y > x:
            greatest = y
        else:
            greatest = str(x) + ', ' + str(z)
    elif y == z and x > y: # Other elif not needed as this is the last possibility
        greatest = x
    else:
        greatest = str(x) + ', ' + str(y) + ', ' + str(z)
'''

if x >= y and x >= z:
    greatest = x
elif y >= x and y >= z:
    greatest = y
else:
    greatest = z
print(greatest)