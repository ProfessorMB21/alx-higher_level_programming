#!/usr/bin/python3
"""
Definition of the save_to_json_file function module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using JSON representation

    Args:
        my_obj (any): object to json representation
        filename (str): file path
    """
    
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)

