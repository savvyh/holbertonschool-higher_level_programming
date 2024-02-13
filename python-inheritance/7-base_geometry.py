#!/usr/bin/python3
"""
    Write a class BaseGeometry based on file 5-base_geometry.py
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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
