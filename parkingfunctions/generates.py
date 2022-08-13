from .validate import pigeonhole_check

from numpy import random

def generator(num_cars=9, num_funcs=1):
    """ Generate parking function(s)
    Parameters:
    num_cars (int): Number of cars in each parking function.
    num_funcs (int): Number of parking functions to generate.
                    Deault is 1, if > 1 will return array of pfs.
    
    Returns:
    Array or Array of Arrays

    """

    number_cars = num_cars
    number_functions = num_funcs
    current_gen = []
    short_func_limit = True

    while short_func_limit:
        x = random.randint(1, int(number_cars) + 1, size=int(number_cars))
        if len(current_gen) >= int(number_functions):
            short_func_limit = False
        elif pigeonhole_check(x):
            current_gen.append(x)

    if number_functions == 1:
        return current_gen[0]
    else:
        return current_gen