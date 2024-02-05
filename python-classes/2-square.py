#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """
        Class that defines a square by is size (private instance attribut)
        Instantiation with optional size, size=0.
    """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
