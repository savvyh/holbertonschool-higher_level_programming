#!/usr/bin/python3
"""
    Function that adds 2 integers
    Write an error if the value a or b is not int or float
    The function converts float to int
"""


def add_integer(a, b=98):
    """
        Check if value is a float or a int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
