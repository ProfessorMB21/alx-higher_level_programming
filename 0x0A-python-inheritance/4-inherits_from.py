#!/usr/bin/python3
"""
Definition of inherits_from function
"""

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class, otherwise False

    Args:
        obj (any): Instance of a class
        a_class (type): class type
    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

