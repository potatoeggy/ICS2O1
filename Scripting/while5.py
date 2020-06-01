# Daniel Chen
# Write a program that calculates the area of a field.  Ask the user to enter the length and width of the field.  Continue to calculate the area for different dimensions until the user enters -1 for the length.
# 26 March 2019

while True:
    l = float(input('Length: '))
    if l == -1.0:
        break
    w = float(input('Width: '))
    print(l * w)