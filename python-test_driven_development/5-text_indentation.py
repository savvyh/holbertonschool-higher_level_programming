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

    new_text = ""
    for char in text:
        new_text += char
        if char in ['.', '?', ':']:
            print(new_text.strip())
            print()
            new_text = ""
    if new_text:
        print(new_text.strip())
