import numpy as np


def pigeonhole_check(park_func):

    """Validates a Parking Function.

    Validates a parking function with pigeonhole principle.

    Args:
        park_func (list): A list representing a parking function.

    Returns:
        bool: If parking function is valid.

    """
    p_n = len(park_func)

    for i in range(p_n):

        m = 0

        for j in park_func:

            if j > p_n:
                return False

            if j >= p_n - i:
                m = m + 1

        if m > i + 1:
            return False

    return True


def get_outcome(park_func):

    """Returns the outcome of a given parking function.

    Takes in a parking function and returns the outcome.

    Args:
        park_func (list): A list representing a parking function.

    Returns:
        list: The outcome of a given parking function.

    """

    if not pigeonhole_check(park_func):
        return "This is not a valid parking function"
    displacement = 0
    func_pi = park_func.copy()

    pi_length = len(func_pi)

    outcome = np.zeros((pi_length,), dtype=int)
    available = np.zeros((pi_length,), dtype=int)

    for i in range(len(func_pi)):

        preferred = func_pi[i]

        for j in range(preferred - 1, len(func_pi)):

            if available[j] == 0:
                outcome[i] = j + 1
                available[j] = 1
                break
            displacement = displacement + 1

    convert_arr = [str(element) for element in outcome]
    outcome_str = ", ".join(convert_arr)
    outcome_str = f"[{outcome_str}]"
    out_dis = [outcome_str, displacement]
    return out_dis
