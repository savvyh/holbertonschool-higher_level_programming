#!/usr/bin/python3
"""test_setter_rectangle.py"""

import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestBase(unittest.TestCase):
    """Test case of the import class Base"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_height_getter(self):
        """Test the property of the height"""
        rect = Rectangle(2, 3, 8, 7, 1)
        self.assertEqual(3, rect.height)

    def test_width_getter(self):
        """Test the property of the width"""
        rect = Rectangle(2, 7, 1, 3, 9)
        self.assertEqual(2, rect.width)

    def test_height_setter(self):
        """Test the setter of the height"""
        rect = Rectangle(1, 9, 3, 15, 6)
        rect.height = 12
        self.assertEqual(12, rect.height)

    def test_width_setter(self):
        """Test the setter of the width"""
        rect = Rectangle(4, 3, 2, 1, 9)
        rect.width = 8
        self.assertEqual(8, rect.width)

    def test_height_setter_negative(self):
        """Test to set a negative int to the height"""
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            rect.height = -8

    def test_width_setter_negative(self):
        """Test to set a negative int to the width"""
        rect = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            rect.width = -8

    def test_height_setter_float(self):
        """Test to set a float to the height"""
        rect = Rectangle(4, 6, 7, 8, 1)
        with self.assertRaises(TypeError):
            rect.height = 3.14

    def test_width_setter_float(self):
        """Test to set a float to the width"""
        rect = Rectangle(4, 6, 7, 8, 1)
        with self.assertRaises(TypeError):
            rect.width = 3.14

    def test_height_setter_string(self):
        """Test to set a string to the height"""
        rect = Rectangle(6, 5, 8, 7, 9)
        with self.assertRaises(TypeError):
            rect.height = "hello"

    def test_width_setter_string(self):
        """Test to set a string to the width"""
        rect = Rectangle(6, 5, 8, 7, 9)
        with self.assertRaises(TypeError):
            rect.width = "hello"

if __name__ == '__main__':
    unittest.main()
