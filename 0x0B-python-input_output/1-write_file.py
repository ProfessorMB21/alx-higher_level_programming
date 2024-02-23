#!/usr/bin/python3
"""
Definition of the write_file function module
"""

def write_file(filename="", text=""):
    """
    Writes a string to a UTF8 text file and returns
    the number of characters written

    Args:
        filename (str): file path
        text (str): string to write to text file
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)

