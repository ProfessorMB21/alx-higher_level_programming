#!/usr/bin/python3

def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary"""

    total = 0
    if isinstance(a_dictionary, dict):
        total = len(a_dictionary.keys())
    return total

