#!/usr/bin/python3
"""Create a class Base"""

import json


class Base:
    """Create class named Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Assign a value to id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        with open(filename, 'w') as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute (id, size, x, y)"""
        if args is not None:
            arguments = ['id', "size", 'x', 'y']
            for key, value in zip(arguments, args):
                setattr(self, key, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""

