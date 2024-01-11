#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set"""

    sym_diff = {}
    if isinstance(set_1, set) and isinstance(set_2, set):
        sym_diff = set_1.symmetric_difference(set_2)
    return sym_diff

