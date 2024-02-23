#!/usr/bin/python3
"""
Definition of the class_to_json function module
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    for JSON serialization of the supplied object

    Args:
        obj: Instance of a class
    """
    return obj.__dict__


