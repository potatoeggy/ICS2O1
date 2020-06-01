# Daniel Chen
# Write a program that will prompt the user for the length of two sides of a right-angled triangle, and calculates and prints the length of the hypotenuse.
# 20 March 2019

from math import sqrt

side1 = float(input('Side 1: '))
side2 = float(input('Side 2: '))

hypo = sqrt(side1 ** 2 + side2 ** 2)
print('Hypotenuse is ' + str(hypo))