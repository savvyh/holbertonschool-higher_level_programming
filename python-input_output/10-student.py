#!/usr/bin/python3
"""defines class Student"""


class Student():
    """class to define student"""

    def __init__(self, first_name, last_name, age):
        """initializes student instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary description for JSON serialization"""
        if isinstance(attrs, list):
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict
        return self.__dict__
