#!/usr/bin/python3
"""Generate Pascal's triangle up to the nth row"""


def pascal_triangle(n):
    """returns a list of lists of integers of the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
