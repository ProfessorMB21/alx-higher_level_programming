#!/usr/bin/python3
"""
Definition of the append_write function module
"""

def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF8 text file
    and returns the number of characters added

    Args:
        filename (str): file path
        text (str): string to append
    """

    with open(filename, mode="a+", encoding="utf-8") as file:
        return file.write(text)

