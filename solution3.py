# Write code for algorithm 3 below
# Write a function that returns the nth elements in the Fibonacci Sequence.


def fibonacci(n):
    if n <= 0:
        return "Invalid input. n should be a positive integer."
    
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        
        fib_1 = 0
        fib_2 = 1
        
        for _ in range(2, n):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
        return fib_2

print(fibonacci(6))

def fibbonaci(n):
  # base cases
  if n == 1:
    return 0
  elif n == 2:
    return 1
  # recursive case
  return fibbonaci(n-1) + fibbonaci(n-2)

print(fibonacci(3))