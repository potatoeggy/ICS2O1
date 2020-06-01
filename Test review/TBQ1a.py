# Daniel Chen
# 21 May 2019
# Amusement park admission program

# Ask for age
age = int(input('Age: '))

# Check set base cost based on age
if 0 <= age <= 2:
    cost = 0
elif 3 <= age <= 17:
    cost = 10
elif 18 <= age <= 64:
    cost = 20
elif age >= 65:
    cost = 12
else:
    print('Invalid age')
    exit()

# Check for pass type
print('Do you want an all-day pass or evening pass?')
print('Enter \'A\' for all-day, \'B\' for evening.')
pass_type = input()

# if necessary convert all-day cost to evening cost
if pass_type.lower() == 'b':
    cost *= 0.75
if pass_type.lower() != 'a' and pass_type.lower() != 'b':
    print('Invalid pass.')

# print results
print('Your pass costs $' + str(cost))