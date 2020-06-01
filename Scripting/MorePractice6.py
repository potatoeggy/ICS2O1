# Daniel Chen
# Prompt the user for two words. If they are the same, print “Great - the same”. If they are the same except for the case, print “Okay - almost the same”. If they are the same length, print “At least the same length”.
# 20 March 2019

word1 = input('Word 1: ')
word2 = input('Word 2: ')
if word1 != word2:
    if word1.lower() == word2.lower():
        print('Okay - almost the same')
else:
    print('Great - the same')

if len(word1) == len(word2):
    print('At least the same length')