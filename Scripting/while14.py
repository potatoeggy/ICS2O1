# Daniel Chen
# A series of marks is to be entered and averaged.  Before you enter the series you are to have the program ask you how many marks there are in the series then read it in.  Test your program to see that it works for series of different lengths, say four marks or six marks.
# 26 March 2019

num = int(input('Number of marks: '))

y = 0
for x in range(0, num):
    x = float(input('Mark ' + str(x + 1) + ': '))
    y = y + x
print(y / num)