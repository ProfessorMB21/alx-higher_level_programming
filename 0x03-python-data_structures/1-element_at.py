#!/usr/bin/python3

def element_at(my_list, idx):
    """Returns an element from a list at the given index"""

    if my_list is None:
        return None
    if idx < 0 or idx > len(my_list):
        return None
    return my_list[idx]

