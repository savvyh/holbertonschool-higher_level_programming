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
        return self.height

    @size.setter
    def size(self, value):
        """Set the value of size"""
        self.height = value
        self.width = value

    def __str__(self):
        """Return a string with all attributes"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")
