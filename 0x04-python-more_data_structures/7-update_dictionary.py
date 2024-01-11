#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary"""

    if isinstance(a_dictionary, dict) and isinstance(key, str):
        if key in a_dictionary.keys():
            a_dictionary[key] = value
        else:
            a_dictionary.update([(key, value)])
    return a_dictionary

