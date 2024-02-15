#!/usr/bin/python3
"""defines function to return an object represented by a JSON string"""

import json


def from_json_string(my_str):
    """return an object represented by a JSON string"""
    return json.loads(my_str)
