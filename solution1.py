# Write code for algorithm 1 below
# Write a program that takes a positive number as an argument and prints the numbers from n to zero.
def count_down(n):
    #base case
    if n == 0:
        return
    
    #recursive case
    print(n)
    count_down(n-1)
    
count_down(7)