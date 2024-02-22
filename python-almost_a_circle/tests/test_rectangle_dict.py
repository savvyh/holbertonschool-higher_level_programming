#!/usr/bin/python3
"""test_area_rectangle.py"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleDict(unittest.TestCase):
    """Test the dict for class Rectangle"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_to_dictionary_with_float(self):
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.x = 10.5

    def test_to_dictionary_with_list(self):
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.y = [1, 2, 3]

    def test_to_dictionary_with_tuple(self):
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.height = (1, 2)

    def test_to_dictionary_with_none(self):
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.width = None


if __name__ == '__main__':
    unittest.main()
