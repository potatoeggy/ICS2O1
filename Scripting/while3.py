# Daniel Chen
# Modify the above program so that it continues to ask the user for a name and outputs the name with a greeting such as <name>,” have a great day” on the screen. The program should stop when the user enters the name “stop”.
# 26 March 2019

while True:
    name = input('Name: ')
    if name.lower() == 'stop':
        break
    print(name + ', have a great day')