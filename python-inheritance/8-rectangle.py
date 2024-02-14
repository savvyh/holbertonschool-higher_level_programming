#!/usr/bin/python3
"""
    Write a class BaseGeometry based on file 7-base_geometry.py
"""


class BaseGeometry:
    """
        Public instance method.

        Raise: Exception if area is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")

    """
        Public instance method.

        Raise: TypeError and ValueError
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
        Defines class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """

        Args:
            width (_type_): _description_
            height (_type_): _description_
        """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
