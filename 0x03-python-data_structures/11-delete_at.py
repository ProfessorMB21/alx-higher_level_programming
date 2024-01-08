#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes an element at the specified index in a list"""

    if idx < 0 or idx > (len(my_list) - 1):
        return my_list


