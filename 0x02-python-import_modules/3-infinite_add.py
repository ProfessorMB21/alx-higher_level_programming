#!/usr/bin/python3
if __name__ == "__main__":
    """prints the result of the addition of all arguments"""
    from sys import *

    argc = argv.__len__()
    result = 0
    for arg in range(1, argc):
        result += int(argv[arg])
    print("{}".format(result))
