#!/usr/bin/python3
"""
Definition of read_file function
"""

def read_fle(filename=""):
    """
    Reads a UTF8 text file and prints to stdout

    Args:
        filename (str): path of text file to read
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

