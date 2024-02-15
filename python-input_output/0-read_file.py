#!/usr/bin/python3
"""
    function that reads a text file
"""


def read_file(filename=""):
    """Args: filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
