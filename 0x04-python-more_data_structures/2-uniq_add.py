#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""

    if isinstance(my_list, list) or len(my_list) == 0:
        return my_list

    no_dup = set(my_list)
    total = 0
    for i in range(len(no_dup)):
        total += i
    return total

