# Name: Daniel Chen
# Date: 6 March 2019
# Description: OV17 - Ask the user for a subject, the total number of marks in a test, and their test mark.  Calculate their test mark as a percent to one decimal place and output the result.

subject = input('Subject: ')
bottomnumber = float(input('Total possible marks on test: '))
topnumber = float(input('Your mark on test: '))

total = round(topnumber / bottomnumber * 100, 1)

print('You scored ' + str(total) + '%' + ' in ' + subject + '.')