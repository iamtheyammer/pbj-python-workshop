age_str = input("How old are you?")
age = 0

try:
  age = int(age_str)
except ValueError:
  print("That age isn't a number!")
  exit(0)