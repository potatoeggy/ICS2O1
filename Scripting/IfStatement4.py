# Daniel Chen
# Fixing code
# 19 March 2019

# Something with this is wrong. What?
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
  print("It is hot outside")
elif temperature > 110: # This will never run as the former if statement will always execute before this one, depriving it of its runningness
  print("Oh man, you could fry eggs on the pavement!")
elif temperature < 30:
  print("It is cold outside")
else:
  print("It is ok outside")
print("Done")