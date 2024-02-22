#!/usr/bin/python3
"""
Definition of is_same_class function
"""

def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class
    Otherwise False

    Args:
        obj (any): Instance of a class
        a_class (type): class type
    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return type(obj) is a_class

