# Daniel Chen
# 30 May 2019
# P1

base = input()

a = int(base.split()[0])
b = int(base.split()[1])

c = int(input())


if a * b == c:
    print('AC')
else:
    print('WA')