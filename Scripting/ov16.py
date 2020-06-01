# Name: Daniel Chen
# Date: 6 March 2019
# Description: OV16 - There are 2.54 cm in one inch.  Write a program to enter the length of a door in inches and output its length in centimetres.  Use a constant for the conversion factor.  Be sure prompt for the input and to label the output.

convert = 2.54
u1 = 'in.' # Enter in this
u2 = 'cm' # Convert to this using 1 u1 per <convert> u2

door = input('Door length in ' + u1 + ': ')
print('Door is ' + str(float(door) * convert) + ' ' + u2 + ' long.')
