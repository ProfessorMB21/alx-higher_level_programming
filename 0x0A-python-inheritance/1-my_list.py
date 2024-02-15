#!/usr/bin/python3
"""
Defintiion of  MyList class
"""


class MyList(list):
    """
    A class that inherits the attributes of class `list`
    """

    def print_sorted(self):
        """
        Prints the list sorted (in ascending order)
        """
        
        list_cpy = self.copy()
        list_cpy.sort()
        print("{}".format(list_cpy))


