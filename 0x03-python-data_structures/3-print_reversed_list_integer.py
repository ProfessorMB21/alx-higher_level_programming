#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""

    if isinstance(my_list, list):
        list_len = len(my_list)
        for i in range(list_len - 1, -1, -1):
            print("{:d}".format(my_list[i]))

