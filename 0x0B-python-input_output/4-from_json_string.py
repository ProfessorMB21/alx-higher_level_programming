#!/usr/bin/python3
"""
Definition of the from_json_string function module
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string

    Args:
        my_str (str): JSON string representing an object
    """
    return json.loads(my_str)

