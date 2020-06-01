# Daniel Chen
# 17 May 2019
# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles triangle has two sides that are the same length, and a third side that is a different length. If all of the sides have different lengths then the triangle is scalene. Write a program that reads the lengths of 3 sides of a triangle from the user. Display a message indicating the type of the triangle.

a = float(input('Side 1: '))
b = float(input('Side 2: '))
c = float(input('Side 3: '))

if a == b and a == c:
    classification = 'equilateral'
elif a != b and a != c and b != c:
    classification = 'scalene'
else:
    classification = 'isosceles'

print('Triangle is ' + classification + '.')