#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""

    if isinstance(a_dictionary, dict):
        new = {key: (a_dictionary[key] * 2) for key in a_dictionary}
        return new

