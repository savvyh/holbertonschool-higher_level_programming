#!/usr/bin/python3
"""
    Function that returns True if the object is exactly
    an instance of a specific class
"""


def is_same_class(obj, a_class):
    """ Check if the object is exactly an instance of a class"""
    return type(obj) is a_class
