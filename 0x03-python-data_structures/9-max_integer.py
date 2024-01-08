#!/usr/bin/python3

def max_integer(my_list=[]):
    """Returns the largest integer in a list"""

    if len(my_list) == 0:
        return

    mid = int(len(my_list) / 2)
    largest = my_list[0]
    for i in range(0, mid):
        if my_list[i] > largest:
            largest = my_list[i]

    for j in range(mid, len(my_list)):
        if my_list[j] > largest:
            largest = my_list[j]

    return largest

