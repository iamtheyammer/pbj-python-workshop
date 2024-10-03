# You'll need the input_number function for this, so I've pasted it here:
def input_number(prompt):
  value = input(prompt)

  try:
    return int(value)
  except ValueError:
    return None

print("> Python Calculator <")

# Ask for the first number
### YOUR CODE HERE ###

# Ask for the operand
operand = input("Do you want to add (+), subtract (-), multiply (*), or divide (/)? ")

# Ask for the second number
### YOUR CODE HERE ###

# Perform the calculation
if operand == "+":
  result = first_number + second_number
### YOUR CODE HERE ###
# What if the operand is invalid?

# Print the result
print(first_number + " " + operand + " " + second_number + " = " + result)