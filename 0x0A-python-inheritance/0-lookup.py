#!/usr/bin/python3
"""
Definition of module 0-lookup
Function that returns the list of available attributes and methods
of an object
"""


def lookup(obj):
    """
    Args:
        obj: instance of a class

    Returns:
        List of attributes and methods
    """

    return dir(obj)

