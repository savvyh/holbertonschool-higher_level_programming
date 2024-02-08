#!/usr/bin/python3
"""
    Function that prints a text with 2 new lines after each of
    these characters: ., ? and :
    Text must be a string
"""


def text_indentation(text):
    """
        Function prints text with 2 new lines after these characters ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    list_characters = [".", "?", ":"]
    for index in text:
        if index in list_characters:
            print(index + "\n\n", end="")
        else:
            print(f"{index}", end="")
