#!/usr/bin/python3
"""
    Write a class BaseGeometry based on file 7-base_geometry.py
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
