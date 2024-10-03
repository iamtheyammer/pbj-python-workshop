print("Let's see if you can legally drink...")
age = input("How old are you? ")

if age < 21:
  diff = 21 - age
  print("Nope! You need to wait " + str(diff) + " more years.")