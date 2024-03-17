# Write code for algorithm 5 below
# Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.
    
def palindrome(str):
  # base cases
  if len(str) == 1 or len(str) == 0:
    return True

  if str[0]!=str[-1]:
    return False

  return palindrome(str[1:-1])

#print(palindrome(338833))