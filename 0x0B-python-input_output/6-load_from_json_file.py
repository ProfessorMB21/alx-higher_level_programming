#!/usr/bin/python3
"""
Definition of load_from_json_file function module
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
        filename (str): file path containing json representation of the object
    """

    with open(filename) as file:
        return json.load(file)

