#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the number and list of the program's command line arguments"""
    from sys import *
    argc = argv.__len__() - 1
    if argc == 1:
        print("{} argument.".format(argc))
    else:
        print("{} arguments.".format(argc))
    for arg in range(1, argc + 1):
        print("{1}: {0}".format(argv[arg], arg))
