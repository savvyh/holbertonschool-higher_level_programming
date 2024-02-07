#!/usr/bin/python3
"""
    Function that prints "my name is" follow by my first name and my last name.
    First name and last name must be string
    Print Error message if not a string
"""


def say_my_name(first_name, last_name=""):
    """
        Function that prints "My name is" follow by first + last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
