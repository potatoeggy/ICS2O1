# Daniel Chen
# Fixing code - c
# 19 March 2019

temperature = int(input("What is the temperature in Fahrenheit? "))
if 110 > temperature > 90: # Fixed here by adding an upper limiit
  print("It is hot outside")
elif temperature > 110:
  print("Oh man, you could fry eggs on the pavement!")
elif temperature < 30:
  print("It is cold outside")
else:
  print("It is ok outside")
print("Done")