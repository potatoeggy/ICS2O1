# Daniel Chen
# January 1st, 2019 is a Tuesday.  Given this information and your knowledge of the days of the week, write a program that takes in a date within 2019 and returns the day of the week (Monday, Tuesday, etc...)
# 21 March 2019

# List solution because elifs are long and I don't know how to use dictionaries
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 
'august', 'september', 'october', 'november', 'december']
daysinmonth = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] # Change for leap year
daysinweek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def day_validation():
    try:
        global day
        day = int(input('Day (e.g.: 1): '))
        if day > 0 and day < 32:
            pass
        else:
            print('Not a valid date. Try again.')
            day_validation()
    except ValueError:
        print('Not an integer. Try again.')
        day_validation()
    except KeyboardInterrupt:
        day_validation()

def month_validation():
    global months
    global dayincurrentmonth
    global printmonth
    month = input('Month (e.g.: January or 1): ')
    if month.lower() in months:
        dayincurrentmonth = daysinmonth[months.index(month.lower())]
        printmonth = month[:1].upper() + month[1:].lower()
    elif int(month) > 0 and int(month) < 13:
        dayincurrentmonth = daysinmonth[int(month) - 1]
        printmonth = months[int(month) - 1]
        printmonth = printmonth[:1].upper() + printmonth[1:].lower()
    else:
        print('Not a month.')
        month_validation()


month_validation()
day_validation()

days = day + dayincurrentmonth
relevant_days = (days + 2) % 7 # Change ' + 2 ' to whatever day of the week to update (e.g.: next year would be +3)
print(str(daysinweek[relevant_days - 1]) + ', ' + printmonth + ' ' + str(day) + ', 2019') # Change to update year

# Longer solution using elif
month = input('Month (e.g.: January or 1): ')
month = month.lower()

day = int(input('Day (e.g.: 1): '))

if day < 0 or day > 32:
    print('Not a valid date.')
    exit()

if month == 'january' or int(month) == 1: # Breaks with leap years
    monthdays = 0
    printmonth = ', January '
elif month == 'february' or int(month) == 2:
    monthdays = 31
    printmonth = ', February '
elif month == 'march' or int(month) == 3:
    monthdays = 59
    printmonth = ', March '
elif month == 'april' or int(month) == 4:
    monthdays = 90
    printmonth = ', April '
elif month == 'may' or int(month) == 5:
    monthdays = 120
    printmonth = ' May '
elif month == 'june' or int(month) == 6:
    monthdays = 151
    printmonth = ', June '
elif month == 'july' or int(month) == 7:
    monthdays = 181
    printmonth = ', July '
elif month == 'august' or int(month) == 8:
    monthdays = 212
    printmonth = ', August '
elif month == 'september' or int(month) == 9:
    monthdays = 243
    printmonth = ', September '
elif month == 'october' or int(month) == 10:
    monthdays = 273
    printmonth = ', October '
elif month == 'november' or int(month) == 11:
    monthdays = 304
    printmonth = ', November '
elif month == 'december' or int(month) == 12:
    monthdays = 334
    printmonth = ', December '
else:
    print('Not a valid month.')
    exit()

days = monthdays + day
relevant_days = (days + 2) % 7 - 1
if relevant_days == 0:
    print('Sunday' + printmonth + str(day) + ', 2019') # Change to update year
elif relevant_days == 1:
    print('Monday' + printmonth + str(day) + ', 2019')
elif relevant_days == 2:
    print('Tuesday' + printmonth + str(day) + ', 2019')
elif relevant_days == 3:
    print('Wednesday' + printmonth + str(day) + ', 2019')
elif relevant_days == 4:
    print('Thursday' + printmonth + str(day) + ', 2019')
elif relevant_days == 5:
    print('Friday' + printmonth + str(day) + ', 2019')
else:
    print('Saturday' + printmonth + str(day) + ', 2019')