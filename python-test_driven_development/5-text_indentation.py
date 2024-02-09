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
    new_line = True
    for index in text:
        if new_line and index == ' ':
            continue
        elif index == '\n':
            new_line = True
        elif index in list_characters:
            print(index + "\n\n", end="")
            new_line = True
        else:
            print(f"{index}", end="")
            new_line = False
