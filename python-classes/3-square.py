#!/usr/bin/python3
"""Create a class Square by is size"""


class Square:
    """
        Private instance attribut : size 
        Instantiation with optional size, size=0.
    """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    """Public instance method that return the current square area"""

    def area(self):
        return self.__size ** 2
