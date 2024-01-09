#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list without modifying the original list
    at a specified index
    """

    if my_list is None:
        return None
    if idx < 0 or idx > (len(my_list) - 1):
        return list(my_list)

    new = list(my_list)
    new[idx] = element
    return new

