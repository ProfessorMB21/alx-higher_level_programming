#!/usr/bin/python3
"""
A Square class definition
"""

class Square:
    """
    A Square class with 2 private instance attributes
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Instatiation with size and position

        Args:
            size (int): size of the square
            position (tuple): coordinates of the square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is True and isinstance(value[1], int) is True:
            if value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        Prints in stdout the square
        """

        if self.__size == 0:
            print("")
        else:
            _x = self.__position[0] * " "
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(_x + ("#" * self.__size))


