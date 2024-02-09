#!/usr/bin/python3
"""
    Function that divides all elements of a matrix.
    Write an error if the matrix is not a list of int or float.
    Also if each row of the matrix is not the same size.
"""


def matrix_divided(matrix, div):
    """
        Function that divides all elements of a matrix.
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    row_length = None
    for row in matrix:
        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(value / div, 2) for value in row] for row in matrix]

    return new_matrix
