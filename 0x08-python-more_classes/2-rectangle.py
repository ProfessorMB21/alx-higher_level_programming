#!/usr/bin/python3
"""
Definition of a Rectangle class
"""

class Rectangle:
    """
    A Rectangle class
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

    def area(self):
        """
        Calculates the area of the rectangle

        Return:
            area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Return:
            the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """
        Getter

        Return:
            the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Args:
            value (int): value to be set as width

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0

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
        Getter

        Return:
            the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            value (int): value to be set as height
        
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
        self.__height = value

