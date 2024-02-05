#!/usr/bin/python3
"""Create a class Square"""


class Square:
    """
        Class that defines a square by is size (private instance attribut)
        Instantiation with size (no type/value verification)
    """

    def __init__(self, size):
        self.__size = size
