#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list"""

    if isinstance(my_list, list) is False or len(my_list) == 0:
        return my_list

    new = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            new.insert(i, replace)
        else:
            new.append(my_list[i])
    return new

