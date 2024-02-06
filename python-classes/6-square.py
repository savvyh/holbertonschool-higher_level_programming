#!/usr/bin/python3
"""Create a class Square by is size"""


class Square:
    """
        Private instance attribut : size
        Instantiation with optional size, size=0.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """Public instance method that return the current square area"""
    def area(self):
        return self.__size ** 2

    """Property to get the size"""
    @property
    def size(self):
        return self.__size

    """Property setter to set the size into value"""
    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    """Prints the square with character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

    """Property to get value of the position"""
    @property
    def position(self):
        return self.__position

    """Property setter to set position into value & check if 2 + integers"""
    @position.setter
    def position(self, value):
        self.__position = value
        if not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")
