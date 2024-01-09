#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all the multiples of 2 in a list"""

    if len(my_list) == 0 or my_list is None:
        return None

    result = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result

