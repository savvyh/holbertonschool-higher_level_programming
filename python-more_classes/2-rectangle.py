#!/usr/bin/python3
"""
    Write a class "Rectangle" that defines a rectangle
    Define height and width
    Calcul the area and perimeter of a rectangle
"""


class Rectangle:
    """
        Initialize the function to create a rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """
        Function that retrieves the height attribute
    """
    @property
    def height(self):
        return self.__height

    """
        Function to set the attribute height
    """
    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    """
        Function that retrieves the width attribute
    """
    @property
    def width(self):
        return self.__width

    """
        Function to set the attribute width
    """
    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    """
        Function that returns the rectangle area
    """
    def area(self):
        return self.__height * self.__width

    """
        Function that returns the rectangle perimeter
    """
    def perimeter(self):
        return (self.__height + self.__width) * 2
