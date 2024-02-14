#!/usr/bin/python3
"""
    Write a class BaseGeometry based on file 7-base_geometry.py
"""


class BaseGeometry:

    def area(self):
        """Raise: Exception if area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Public instance method.
            Raise: TypeError and ValueError
        """
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

    def __str__(self):
        """return a rectangle description"""
        return (str("[Rectangle] {}/{}".format(self.__width, self.__height)))

    def area(self):
        """implemented the area method"""
        return (self.__width * self.__height)


class Square(Rectangle):
    """Write a class that inherits from Rectangle"""

    def __init__(self, size):
        """Args: size (_type_): _description_"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """implemented the area method"""
        return (self.__size ** 2)
