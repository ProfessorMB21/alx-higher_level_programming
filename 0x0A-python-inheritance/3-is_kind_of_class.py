#!/usr/bin/python3
"""
Definition of is_kind_of_class function
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class

    Args:
        obj (any): Instance of a class
        a_class (type): Class type
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False

