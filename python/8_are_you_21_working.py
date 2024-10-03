def input_number(prompt):
  value = input(prompt)

  try:
    return int(value)
  except ValueError:
    return None
  
print("Let's see if you can legally drink...")
age = input_number("How old are you? ")

if age is None:
  print("You didn't enter a number!")
elif age < 21:
  diff = 21 - age
  print("Nope! You need to wait " + str(diff) + " more years.")
else:
  print("Yep! Go out and have fun.")