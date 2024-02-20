#!/usr/bin/python3
"""Create a class Base"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Assign a value to id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
