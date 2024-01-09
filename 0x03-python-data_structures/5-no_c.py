#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c and C from a string"""

    if len(my_string) == 0 or my_string is None:
        return None

    new = ""
    for c in range(len(my_string)):
        if my_string[c] =! 'c'and my_string[c] == 'C':
            new += my_string[c]
    return new

