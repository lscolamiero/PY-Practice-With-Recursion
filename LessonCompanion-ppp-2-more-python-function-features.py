#Exercise 1: Python Functions using **kwargs
#*args allows a function to accept any number of unnamed arguments of any type. **kwargs allows a function to accept any number of named arguments of any type.

#Exercise 2: Python Functions using **kwargs
#Define a function named manyParams() that accepts any number of named parameters. The function should return three lists: a list of all the string parameters, a list of any numerical parameters (each incremented by three), and a list of any non-string and non-numerical parameters.

def manyParams(*args, **kwargs):
    string_params = []
    numerical_params = []
    non_string_numerical_params = []

    for arg in args:
        if isinstance(arg, str):
            string_params.append(arg)
        elif isinstance(arg, (int, float)):
            numerical_params.append(arg + 3)
        else:
            non_string_numerical_params.append(arg)

    for key, value in kwargs.items():
        if isinstance(value, str):
            string_params.append(value)
        elif isinstance(value, (int, float)):
            numerical_params.append(value + 3)
        else:
            non_string_numerical_params.append(value)

    return string_params, numerical_params, non_string_numerical_params

# Example usage:
strings, numbers, others = manyParams(5, 'hello', 8.5, name='John', age=30, city='New York')
print("Strings:", strings)
print("Numerical params incremented by 3:", numbers)
print("Non-string and non-numerical params:", others)
def manyParams(**kwargs):
  string_params = []
  numerical_params = []
  other_params = []

  for val in kwargs.values():
    if isinstance(val, str):
      string_params.append(val)
    elif isinstance(val, int):
      numerical_params.append(val)
    else:
      other_params.append(val)

  return string_params, numerical_params, other_params

#Exercise 3: Combining Python Function Features
#In terms of argument handling, it is accurate to say that Python functions:
# Demonstrate flexibility by accepting positional arguments, default arguments, and keyword arguments. JWT

#Exercise 4: Built-in Python Functions
#Where can a comprehensive list of built-in Python functions be found?
# docs.python.org