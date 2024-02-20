#!/usr/bin/python3
"""test_area_rectangle.py"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestArea(unittest.TestCase):
    """ test area for class rectangle.py """

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_height_is_negative(self):
        """Test with a negative height"""
        with self.assertRaises(ValueError):
            Rectangle(7, -3)

    def test_width_is_negative(self):
        """Test with a negative width"""
        with self.assertRaises(ValueError):
            Rectangle(-7, 3)

    def test_both_negative(self):
        """Test with negatives width and height"""
        with self.assertRaises(ValueError):
            Rectangle(-7, -3)

    def test_height_is_float(self):
        """Test with a float height"""
        with self.assertRaises(TypeError):
            Rectangle(3, 5.5)

    def test_width_is_float(self):
        """Test with a float width"""
        with self.assertRaises(TypeError):
            Rectangle(3.3, 5)

    def test_both_float(self):
        """Test with float width and height"""
        with self.assertRaises(TypeError):
            Rectangle(3.3, 5.5)

    def test_height_is_string(self):
        """Test with a string height"""
        with self.assertRaises(TypeError):
            Rectangle(3, "everybody")

    def test_width_is_string(self):
        """Test with a string width"""
        with self.assertRaises(TypeError):
            Rectangle("hi", 5)

    def test_both_string(self):
        """Test with strings width and height"""
        with self.assertRaises(TypeError):
            Rectangle("hi", "everybody")


if __name__ == '__main__':
    unittest.main()
