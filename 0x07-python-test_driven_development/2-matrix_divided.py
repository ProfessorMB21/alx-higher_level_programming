#!/usr/bin/python3
""" Defines a matrix division function """

def matrix_division(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix (list): a list of lists of integers or floats
        div (int/float): the divisor of the matrix

    Raises:
        TypeError: If the matrix is not a list
        TypeError: If rows of the matrix are not of the same size
        TypeError: If div is not a int or float
        TypeError: If matrix contains a non-int or non-float
        ZeroDivisionError: if div is 0

    Returns:
        A new matrix after division, with all elements rounded to 2 d.p
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

