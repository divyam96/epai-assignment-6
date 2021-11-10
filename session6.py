import math


def check_docstring():
    """
    This function has been written to check if the docstring of an input function has greater than fifty \
    characters.
    """
    # Defining the minimum criteria length for docstring length
    doclength = 50

    def inner(func):
        # Using the docstring as a free variable
        nonlocal doclength
        # C1: To check if the input function is valid
        if callable(func) == False:
            raise TypeError("Please enter a valid function")
        ret = False
        # C2:To check if docstring is empty or not
        if bool(func.__doc__) == True:
            a = len(func.__doc__)
            print(a)
            if a >= doclength:
                ret = True
            else:
                pass
        else:
            pass
        return ret
    return inner


def get_fibonacci_number():
    """
    This function has been written to check if an input number is a Fibonacci one and to generate the next Fibonacci number.
    """
    # Test to check for a perfect square
    func = lambda x: (int(math.sqrt(x)) ** 2) == x
    # Formula to calculate the next Fibonacci number
    nextfibonacci = lambda y: y *(1 + math.sqrt(5))/2

    def generate_fibonacci(numinp):
        if isinstance(numinp, int) == False:
            raise TypeError("Please enter an integer only")
        if numinp < 1:
            raise ValueError("Enter a number equal to or greater than 1")
        if (func((5 * (numinp ** 2) + 4)) != True) and (func((5 * (numinp ** 2) - 4)) != True):
            raise ValueError("The input is not a Fibonacci number")
        return round(nextfibonacci(numinp))

    return generate_fibonacci


# Beginning of code corresponding to the third question of the assignment
dictionary_of_functions = {}


def track_arth_count(fn):
    """This function has been written in order to count how many times a few allowed functions - 'add', 'mul' and 'div' - have \
    been called, and the respective counts are stored as values in a dictionary, with the corresponding function names acting as the keys."""
    if callable(fn) == False:
        raise TypeError("Please enter a valid function")
    if fn.__name__ not in ['add', 'mul', 'div']:
        raise ValueError("Only the count of add, mul, div are being monitored")


    def inner(*args, **kwargs):
        if bool(args) == False:
            raise TypeError("Please enter required positional arguments")
        if fn.__name__ in ['add','mul','div']:
            if fn.__name__ not in dictionary_of_functions:
                dictionary_of_functions[fn.__name__] = 0
            dictionary_of_functions[fn.__name__] += 1
        return fn(*args, **kwargs)
    return inner


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    return a/b


def new_input_dictionary(fn, custom_dict):
    """This function has been written to take a dictionary - similar to the one created in the function track_arth_count \
    - as input, and counting the number of times 'add', 'mul' and 'div' have been called."""
    if callable(fn) == False:
        raise TypeError("Please enter a valid function")
    if (type(custom_dict) is dict) == False:
        raise TypeError("Please input only a dictionary")
    if fn.__name__ not in ['add', 'mul', 'div']:
        raise ValueError("Only add, mul, div are allowed")

    def inner(*args, **kwargs):
        if bool(args) == False:
            raise TypeError("Please enter required positional arguments")
        if fn.__name__ in ['add','mul','div']:
            if fn.__name__ not in custom_dict:
                custom_dict[fn.__name__] = 0
            custom_dict[fn.__name__] += 1
        return fn(*args, **kwargs)
    return inner

