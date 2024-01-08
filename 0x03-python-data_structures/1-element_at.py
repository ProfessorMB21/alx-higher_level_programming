#!/usr/bin/python3

def element_at(my_list, idx):
    """Returns an element from a list at the given index"""

    if idx < 0 or idx > len(my_list):
        return
    return my_list[idx]

