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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
