#!/usr/bin/python3
"""
Definition of a Rectangle class
"""


class Rectangle:
    """
    A Rectangle class with 2 private instance attributes
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation with width and height

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter of width

        Return:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter

        Args:
            value (int): value to set as width

        Raises:
            TypeError: If value is not an integer
            ValueError: if value is less than 0

        Return:
            None
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter of height

        Return:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter

        Args:
            value (int): value to set as height

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0

        Return:
            None
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height == value


