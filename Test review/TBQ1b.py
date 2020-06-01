# Daniel Chen
# 21 May 2019
# Amusement park admission program looped

infants = 0
children = 0
adults = 0
seniors = 0
children_money = 0
adult_money = 0
senior_money = 0

while True:
    # Ask for age and quit
    age = int(input('Age (-1 to exit): '))
    if age == -1:
        break

    # Check set base cost based on age
    if 0 <= age <= 2:
        cost = 0
        infants += 1
        payer = 'infant'
    elif 3 <= age <= 17:
        cost = 10
        children += 1
        payer = 'children'
    elif 18 <= age <= 64:
        cost = 20
        adults += 1
        payer = 'adult'
    elif age >= 65:
        cost = 12
        seniors += 1
        payer = 'senior'
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
        exit()

    if payer == 'children':
        children_money += cost
    elif payer == 'adult':
        adult_money += cost
    elif payer == 'senior':
        senior_money += cost

    # print results
    print('Your pass costs $' + str(cost))

print(str(infants) + ' infants were admitted.')
print(str(children) + ' children were admitted at a cost of ' + format(children_money, '.2f') + '.')
print(str(adults) + ' adults were admitted at a cost of ' + format(adult_money, '.2f') + '.')
print(str(seniors) + ' seniors were admitted at a cost of ' + format(senior_money, '.2f') + '.')