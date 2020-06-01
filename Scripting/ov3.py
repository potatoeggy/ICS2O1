# Name: Daniel Chen
# Date: 6 March 2019
# Description: OV3 - Calculates 13% tax on purchase of $12.99

bill = 12.99
tax_human_readable = 13
tax = 0.13

print('You owe $' + str(round(tax * bill, 2)) + ' tax on a purchase of $' + str(bill) + ' at ' + str(tax_human_readable) + '%, giving a total of $' + str(round(bill + bill * tax, 2)))