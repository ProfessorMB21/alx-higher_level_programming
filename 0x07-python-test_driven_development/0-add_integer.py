#!/usr/bin/python3
""" Defines a function that adds 2 integers """

def add_integers(a, b=98):
    """
    Returns the addition of two integers

    Floats are typecastted to int before adding them.

    Raises:
        TypeError: If either a or b is not of type int or float.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

