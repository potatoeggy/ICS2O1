# Daniel Chen
# Two end character inverter
# 20 March 2019

word = input('Word: ')
first = word[-2:-1].upper()
middle = word[-1:]
end = word[:-2].lower()
print(first + middle + end)