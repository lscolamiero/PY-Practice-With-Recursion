# Write code for algorithm 4 below
# Write a function that calculates the value of 'a' to the power of 'b'.

def exponent(a, b):
  # base case
  if b == 1:
    return a

  # recursive case
  return a * exponent(a, b-1)