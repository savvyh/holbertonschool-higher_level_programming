#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
        Function that returns True if the object is exactly
        an instance of a specific class
    """
    return type(obj) is a_class
