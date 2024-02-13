#!/usr/bin/python3
"""
    Class MyList that inherits from list
"""


class MyList(list):
    """Function that sort a list inside a new list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
