#!/usr/bin/python3
"""
    Function that returns True if an object is an instance of a class
    that inherited (directly or indirectly) from the specific class
"""


def inherits_from(obj, a_class):
    """ check if an instance is from a class or inherited a specific class """
    return isinstance(obj, a_class) and type(obj) is not a_class
