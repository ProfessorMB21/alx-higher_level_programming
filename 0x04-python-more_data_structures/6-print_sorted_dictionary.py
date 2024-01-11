#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""

    if isinstance(a_dictionary, dict):
        sorted_ = {}
        sort_keys = []

        for k in a_dictionary.key():
            sort_keys.append(k)
        sorted_.update(sorted(sort_keys))

        for k in sorted_.keys():
            print("{}: {}".format(k, sorted_[k]))

