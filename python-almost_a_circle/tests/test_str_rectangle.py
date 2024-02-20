#!/usr/bin/python3
"""test_rectangle.py"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestStrRectangle(unittest.TestCase):
    """Test case of the __str__ method of the rectangle"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_str_method(self):
        """Test with integer id"""
        test = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(test), "[Rectangle] (12) 2/1 - 4/6")

    def test_id_none(self):
        """Test with a None id"""
        test = Rectangle(10, 10, 10, 10, None)
        self.assertEqual(str(test), "[Rectangle] (1) 10/10 - 10/10")

    def test_id_string(self):
        """Test with an id string"""
        with self.assertRaises(TypeError):
            Rectangle(5, 4, 3, 2, 1, "hello")

    def test_id_float(self):
        """Test with an id float"""
        with self.assertRaises(TypeError):
            Rectangle(5, 4, 3, 2, 1, 8.75)


if __name__ == '__main__':
    unittest.main()
