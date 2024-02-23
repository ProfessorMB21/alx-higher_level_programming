#!/usr/bin/python3
"""
Definition of class Rectangle inheriting from BaseGeometry
(7-base_geometry.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The Rectangle class inheriting from base class BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instatiation with width and height
        Validates the width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = width

