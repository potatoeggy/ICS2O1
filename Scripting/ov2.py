# Name: Daniel Chen
# Date: 6 March 2019
# Description: OV2 - Outputs area of rectangle with dimensions of 5m x 4m

# Setting length, width, and unit of measurement (singular)

l = 5
w = 4
u = ' metre'

if l * w != 1:
    pluralu = u + 's'

# Printing "The area of a <length> by <width> <unit> rectangle is <area> <plural units>."
print('The area of a ' + str(l) + ' by ' + str(w) + u + ' rectangle is ' + str(l * w) + pluralu + '.')