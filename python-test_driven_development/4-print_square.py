#!/usr/bin/python3
"""
    Function that prints a square with the character #.
    Size is the length of the square
    size must be an integer.
    check if the size is less than 0 or if is a float and less than 0
"""


def print_square(size):
    """
        print a square with #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    elif size is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
