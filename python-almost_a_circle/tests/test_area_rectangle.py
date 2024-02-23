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

    def test_negative_assignment(self):
        """Test with a negative assignment"""
        with self.assertRaises(ValueError):
            Rectangle(7, -3)
        with self.assertRaises(ValueError):
            Rectangle(-7, 3)
        with self.assertRaises(ValueError):
            Rectangle(-7, -3)

    def test_float_assignment(self):
        """Test with a float assignment"""
        with self.assertRaises(TypeError):
            Rectangle(3, 5.5)
        with self.assertRaises(TypeError):
            Rectangle(3.3, 5)
        with self.assertRaises(TypeError):
            Rectangle(3.3, 5.5)

    def test_string_assignment(self):
        """Test with a string assignment"""
        with self.assertRaises(TypeError):
            Rectangle(3, "everybody")
        """Test with a string width"""
        with self.assertRaises(TypeError):
            Rectangle("hi", 5)
        with self.assertRaises(TypeError):
            Rectangle("hi", "everybody")

    def test_area_rectangle(self):
        """tets area of the rectangle"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


if __name__ == '__main__':
    unittest.main()
