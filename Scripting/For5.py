# Daniel Chen
# Write program so that it prints the numbers 1 to 15. After outputting, the program should also output the sum and the average of the numbers between and 1 to 15.
# 22 March 2019

num = 15
y = 0
z = 0

for x in range(1, num + 1):
    print(x)
    y = y + x
    z = z + x
print(y) # total
print(z / num) # average