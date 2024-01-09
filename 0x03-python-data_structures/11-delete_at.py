#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes an element at the specified index in a list"""

    if len(my_list) == 0 or my_list is None:
        return my_list

    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    my_list.__delitem__(idx)
    return my_list
