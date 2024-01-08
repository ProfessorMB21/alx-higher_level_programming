#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""

    for i in range(len(matrix)):
        cols = len(matrix[i])
        for j in range(cols):
            print("{:d}".format(matrix[i][j]), end=" ")
        print("")

