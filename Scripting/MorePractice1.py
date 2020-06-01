# Daniel Chen
# Assume that the days of the week are numbered 0, 1, 2, 3, 4, 5, 6 from Sunday to Saturday.  Write a program that asks for a day number, and prints the day name (a string)

# Easy way with lists
name = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
num = int(input('Number: '))
if num > 6 or num < 0:
    print('Out of range')
else:
    print(name[num])

# Longer way with if
num = int(input('Number: '))
if num > 6 or num < 0:
    print('Out of range')
elif num == 0:
    print('Sunday')
elif num == 1:
    print('Monday')
elif num == 2:
    print('Tuesday')
elif num == 3:
    print('Wednesday')
elif num == 4:
    print('Thursday')
elif num == 5:
    print('Friday')
else:
    print('Saturday')