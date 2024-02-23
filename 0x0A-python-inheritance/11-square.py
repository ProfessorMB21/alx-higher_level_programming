#!/usr/bin/python3
"""
Definition of class Square inheriting from class Rectangle
(task based on 10-square.py)
"""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
    A Square class inheriting from base class Rectangle
    """

    def __init__(self, size):
        """
        Instatiation with size
        Validates size

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the shape
        """
        return str("[Square] {}/{}".format(self.__size, self.__size))

