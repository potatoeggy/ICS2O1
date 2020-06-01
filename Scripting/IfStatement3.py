# Daniel Chen
# Asks for input and prints it is hot outside when Fahrenheit is over 90, cold under 30, and not hot between the two.
# 19 March 2019

temp = float(input('Temperature in Fahrenheit: '))

if temp > 90:
    print('It is hot outside.')
elif temp < 30:
    print('It is cold outside.')
else:
    print('It is not hot outside.')
print('Done.')