#!/usr/bin/python3
""" Defines a function that prints a square """

def print_square(size):
    """
    Prints a square with the character '#'

    Args:
        size (int): the size of the square

    Raises:
        TypeError: If size is not an integer
        TypeError: If size is float and less than 0
        ValueError: If value of size is less than 0

    """
    
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

