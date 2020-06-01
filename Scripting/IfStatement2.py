# Daniel Chen
# Asks for input and prints it is hot outside when Fahrenheit is over 90 and it is not hot otherwise.
# 19 March 2019

temp = float(input('Temperature in Fahrenheit: '))

if temp > 90:
    print('It is hot outside.')
elif temp < 90:
    print('It is not hot outside.')
else:
    print('It is exactly 90 degrees Fahrenheit.')
print('Done.')