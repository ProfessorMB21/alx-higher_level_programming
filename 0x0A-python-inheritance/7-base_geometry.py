#!/usr/bin/python3
"""
Definition of class BaseGeometry
"""


class BaseGeometry:
    """
    The BaseGeometry class
    """
    

    def area(self):
        """
        Initializing area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if value is an integer, otherwise raises an exception

        Args:
            name (str): name
            value (int): integer
        Raises:
            TypeError: if name is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

