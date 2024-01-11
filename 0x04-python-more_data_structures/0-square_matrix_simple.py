#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square values of all integerges of a matrix"""

    if isinstance(matrix, list) is False or len(matrix) == 0:
        return matrix

    new = []
    for i in range(len(matrix)):
        sub = []
        for j in range(len(matrix[i])):
            sub.append(squared(matrix[i][j]))
        new.append(sub)

    return new

def squared(num):
    """Squares an integer"""
    return num**2

