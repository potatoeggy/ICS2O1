# Daniel Chen
# Ask the user for an integer at which to start counting.  Ask the user for an integer at which to stop counting.  Count from start up to stop by 1s by printing those numbers out.
# 22 March 2019

start = int(input('Integer 1: '))
end = int(input('Integer 2: '))

for x in range(start, end + 1):
    print(x)