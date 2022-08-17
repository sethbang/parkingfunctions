from .validate import pigeonhole_check

from numpy import random

def generator(num_cars=9, num_funcs=1):

    """Generates list of parking functions.

    Generates and returns a list of size num_funcs of
    valid parking functions [pf] each of desired length num_cars.

    Args:
        num_cars (int): Int representing the size of individual pfs. 
        num_funcs (int): Int representing the number of pfs returned.

    Returns:
        list: A list of randomly generated valid parking functions.

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