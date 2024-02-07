#!/usr/bin/python3
"""
    Function that divides all elements of a matrix.
    Write an error if the matrix is not a list of int or float.
    Write an error if each row of the matrix is not the same size.
    All function must be divided by div.
    Div must be a number et can't be equal to 0.
"""
def matrix_divided(matrix, div):
    new_matrix = []

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    row_length = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")  
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)
    
    return new_matrix
