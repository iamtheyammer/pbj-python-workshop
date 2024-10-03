def say_hello(name):
  print("Hello, " + name + "!")

say_hello("Sam")
say_hello("Annie")

def input_number(prompt):
  value = input(prompt)

  try:
    return int(value)
  except ValueError:
    return None
  
print(input_number("Enter a number: "))
print(type(input_number("Enter another number: ")))