# Daniel Chen
# You go on a vacation leaving on day number 3 (a Wednesday).  You return home after 15 sleeps, then you will be returning on a Thursday.  Write a program that will prompt the user for the starting day of the week and the length of the vacation (# of nights), then calculate and print the name of the day you will return on.
# 20 March 2019

start = int(input('Day of the week: '))
if start < 0 or start > 6:
    print('Out of range')
    exit()
    
nights = int(input('Number of nights: '))

if nights > 6:
    endday = nights % 7 + start
else:
    endday = nights + start
if endday > 6:
    endday = endday % 6

# Lists solution
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(days[endday])

# elif solution
if endday == 0:
    print('Sunday')
elif endday == 1:
    print('Monday')
elif endday == 2:
    print('Tuesday')
elif endday == 3:
    print('Wednesday')
elif endday == 4:
    print('Thursday')
elif endday == 5:
    print('Friday')
else:
    print('Saturday')