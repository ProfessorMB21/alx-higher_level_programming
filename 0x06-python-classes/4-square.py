#!/usr/bin/python3
"""
A Square class definition
"""

class Square:
    """
    A Square class with a getter and setter
    """

    def __init__(self, size=0):
        """
        Instantiation with size

        Args:
            size (int): size of the square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Retrieves the value of size
        """

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

