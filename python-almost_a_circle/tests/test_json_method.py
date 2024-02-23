#!/usr/bin/python3
"""Unittest for to_json_string and from_json_string methods"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestJSONMethods(unittest.TestCase):
    """Test case for to_json_string and from_json_string methods"""

    def setUp(self):
        """Reset Base._Base__nb_objects before each test"""
        Base._nb_objects = 0

    def test_json_to_dict(self):
        """Test the json method"""
        list_input = [
         {'id': 89, 'width': 10, 'height': 4},
         {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), type(list()))
        self.assertEqual(list_input, [{'height': 4, 'width': 10, 'id': 89},
                                      {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(type(json_list_input), type(str()))
        self.assertEqual(json_list_input,
                         '[{"id": 89, "width": 10, "height": 4},\
 {"id": 7, "width": 1, "height": 7}]')
        self.assertEqual(type(list_output), type(list()))
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89},
                                       {'height': 7, 'width': 1, 'id': 7}])


if __name__ == "__main__":
    unittest.main()
