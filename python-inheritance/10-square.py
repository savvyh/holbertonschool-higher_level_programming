#!/usr/bin/python3
"""
    Import class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Write a class that inherits from Rectangle"""

    def __init__(self, size):
        """Args: size (_type_): _description_"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """implemented the area method"""
        return (self.__size * self.__size)
