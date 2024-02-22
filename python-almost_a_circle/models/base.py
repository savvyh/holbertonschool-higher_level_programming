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
