#!/usr/bin/python3
"""
Square Class Definition
"""

class Square:
    """
    Square Class representation with private attribute
    """

    def __init__(self, size=0):
        """
        Initialising Square class

        Args:
            size (int): Size of the Square
        Raises:
            TypeError: if size is not int
            ValueError: if size is < 0
        """

        if type(size) is not int:
            raise TypeError("size must be int")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

