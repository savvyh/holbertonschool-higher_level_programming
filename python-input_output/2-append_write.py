#!/usr/bin/python3
"""
    function that append a string at the end of a text file
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
