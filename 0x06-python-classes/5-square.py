#!/usr/bin/python3
"""
A Square class definition
"""


class Square:
    """
    A Square class with 2 public instance methods
    """

    def __init__(self, size=0):
        """
        Instatiation with size

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

        return (self__size * self.__size)

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

    def my_print(self):
        """
        Prints in stdout the square
        """

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)


