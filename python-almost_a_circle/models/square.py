#!/usr/bin/python3
"""Create a class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class named Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Call the super class of the Rectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the value of size

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0."""
        self.width = value
        self.height = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def __str__(self):
        """Return a string with all attributes"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")

    def update(self, *args, **kwargs):
        """Assigns attributes for *args and **kwargs"""
        args = ("self.id", "self.size", "self.x", "self.y")

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute (id, width, height, x, y)"""
        if args is not None:
            arguments = ['id', "size", 'x', 'y']
            for key, value in zip(arguments, args):
                setattr(self, key, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionnary representation of a Square"""
        square_dict = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
        return square_dict
