#!/usr/bin/python3
"""Create a class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """A class rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x of the top-left corner of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x of the top-left corner of the rectangle.

        Args:
            value (int): The x value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y of the top-left corner of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y of the top-left corner of the rectangle.

        Args:
            value (int): The y value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the character #"""
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string with all attributes"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -"
                f" {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute (id, width, height, x, y)"""
        if args is not None:
            arguments = ['id', 'width', 'height', 'x', 'y']
            for key, value in zip(arguments, args):
                setattr(self, key, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        rectangle_dict = {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width
        }
        return (rectangle_dict)
