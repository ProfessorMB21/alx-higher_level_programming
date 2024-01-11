#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary"""

    if isinstance(a_dictionary, dict) and isinstance(key, str):
        if key in a_dictionary.keys():
            a_dictionary.__delitem(key)
    return a_dictionary

