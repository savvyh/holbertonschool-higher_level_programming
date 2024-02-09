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

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    """
        Function that print the rectangle with the character #
    """
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ('')
        return '\n'.join([str(self.print_symbol) * self.__width]
                         * self.__height)

    """
        Function that returns a string representation of the rectangle
        to be able to recreate a new instance by using eval() inside the main
    """
    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    """
        Function that delete the instance Rectangle
    """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """
        Function that return the biggest rectangle based on the area
    """
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    """
        Class method that returns a new Rectangle instance with :
        width == height == size
    """
    def square(cls, size=0):
        return (cls.size, size)
