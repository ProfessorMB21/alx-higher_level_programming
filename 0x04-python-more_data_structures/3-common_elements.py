#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets"""

    intersect = {}
    if isinstance(set_1, set) and isinstance(set_2, set):
        intersect = set_1.intersection(set_2)
    return intersect


