# Daniel Chen
# 17 May 2019
'''
A particular cell phone plan includes 50 minutes of air time and 50 text messages for $15.00/month. Each additional minute of air time costs $0.25, while additional text messages cost $0.15 each. All cell phone bills include an additional charge of $0.44 to support 911 call centers, and the entire bill (including the 911 charge) is subject to 5% sales tax.

Write a program that prompts the user to enter the number of minutes and text messages used in a month. Display the base charge, additional minutes charge (if any), additional text message charge (if any), the 911 fee, tax and total bill amount. Only display the additional minute and text message charges if the user incurred costs in these categories. Ensure that all of the charges are displayed using 2 decimal places.
'''
# copy as var
base_price = 15.00
extra_minute_price = 0.25
extra_message_price = 0.15
tax_price = 1.05
emergency_support_price = 0.44

# initialise
extra_minutes = 0
extra_messages = 0

# input
minutes = float(input('Minutes/month: '))
messages = int(input('Messages/month: '))

if minutes == 0:
    emergency_support_price = 0


if minutes < 0 or messages < 0:
    print('Invalid entry.')
    exit()

if minutes > 50:
    extra_minutes = minutes - 50

if messages > 50:
    extra_messages = messages - 50

total = (base_price + extra_minute_price * extra_minutes + extra_message_price * extra_messages + emergency_support_price)
taxed_total = total * tax_price

print('Base price is $' + format(base_price, '.2f'))

if extra_minutes != 0:
    print(str(extra_minutes) + ' extra minutes have been charged $' + format(extra_minute_price * extra_minutes, '.2f'))

if extra_messages != 0:
    print(str(extra_messages) + ' extra messages have been charged $' + format(extra_message_price * extra_messages, '.2f'))

if emergency_support_price != 0:
    print('Emergency services support price is $' + str(emergency_support_price))

print('5% tax has been charged at $' + format(taxed_total - total, '.2f'))
print('You have been charged $' + format(taxed_total, '.2f'))