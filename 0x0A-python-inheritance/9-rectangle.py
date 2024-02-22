#!/usr/bin/python3
"""
Definition of class Rectangle inheriting from BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class inheriting from BaseGeometry class
    """

    def __init__(self, width, height):
        """
        Instatiation with width and height
        Validating height and width

        Args:
            width (int): width of rect
            height (int): height of rect
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string represetation of the object
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

