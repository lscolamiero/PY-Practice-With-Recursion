#1 arb_args - Takes in any number of arguments and prints them one at a time.

def arbitrary_args(*args):
    for a in args:
        print(a)

arbitrary_args('Lautaro', 2, True, 'What?')

#2 inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(a, b):
    def operation1(x, y):
        return x + y  

    def operation2(x, y):
        return x * y  
    
    print(operation1(a, b) + operation2(a, b))
    
inner_func(1,2)

#3 lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)
    
lunch_lady('Joe', 'Sloppy sandwich')
lunch_lady('Jill') 

#4 sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(x, y):
    return (x + y), (x * y)

print(sum_n_product(54, 100))

#5 alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.



#6 arb_mean - Accepts any number of integers and prints their average.


#7 arb_longest_string - Accepts any number of strings and returns the longest one.