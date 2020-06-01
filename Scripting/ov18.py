# Name: Daniel Chen
# Date: 6 March 2019
# Description: OV18 - Have the user enter the radius of a circle (accurate to two decimals) and output the circumference (accurate to three decimal places)

pi = 3.14159
r = round(float(input('Radius to 2 decimal points: ')), 2)
C = round(pi * 2 * r, 3)

print('The circumference of a circle with a radius of ' + str(r) + ' is ' + str(C) + '.')