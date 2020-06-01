# Daniel Chen
# Final mark calculator via course mark and exam mark
# 19 March 2019

course = float(input('Course percentage: '))
exam = float(input('Exam percentage: '))

if exam > 100 or exam < 0 or course > 100 or course < 0:
    print('Value not accepted')
    exit()

final = course * 0.7 + exam * 0.3
if final >= 50 and exam >= 60:
    print('You passed with a final mark of ' + str(final) + '%')
elif exam <= 60:
    print('You failed your exam.')
else:
    print('You failed with a final mark of ' + str(final) + '%')