#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specified index"""

    if idx < 0 or idx > len(my_list):
        return my_list
    my_list[idx] = element

