# Name: Daniel Chen
# Date: 6 March 2019
# Description: OV19 - You are investing money (principal) for a certain rate (%) for a number of years (time).  Write a program that calculates the interest you would earn.   Be sure to round the amount to the nearest cent.

principal = float(50) # in dollars only
rate = float(0.15)
years = float(8)

interest = round(principal * rate * years, 2)

print('You earn $' + str(interest) + ' over ' + str(years) + ' years at ' + str(rate * 100) + '%' + ' interest with a principal of $' + str(principal) + '.')