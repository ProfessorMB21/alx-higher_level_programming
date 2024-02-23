#!/usr/bin/python3
"""
Definition of the to_json_string function module
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj (any): object
    """
    return json.dumps(my_obj)

