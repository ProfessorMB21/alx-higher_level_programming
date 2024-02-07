#!/usr/bin/python3
"""
Definition of a Rectangle class based on 4-rectangle.py
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
            Area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Return:
            Perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """
        Getter

        Return:
            Width of rectangle
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
            Height of rectangle
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
            ValueError:If value is less than 0

        Return:
            None
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        Returns a printed rectangle

        Return:
            A printed rectangle with `#`
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        return (('#' * self.__width + "\n") * self.__height)[:-1]
    
     def __repr__(self):
        """
        Returns the string representation of the rectangle

        Return:
            A string representation of the rectangle
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
    
    def __del__(self):
        """
        Prints a message after deletion of a Rectangle instance

        Return:
            A string
        """
        print("Bye rectangle...")

