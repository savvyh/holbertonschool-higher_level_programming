#!/usr/bin/python3
"""
    function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
