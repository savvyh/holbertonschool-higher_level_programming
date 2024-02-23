#!/usr/bin/python3
"""test_setter_rectangle.py"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestSetterRectangle(unittest.TestCase):
    """Test case of the import class Base"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_height_getter(self):
        """Test the property of the height"""
        rect = Rectangle(2, 3, 8, 7, 1)
        self.assertEqual(3, rect.height)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(3.14, 5, 7, 8, 1)
        with self.assertRaises(TypeError):
            Rectangle("hello", 5, 8, 7, 9)
        with self.assertRaises(TypeError):
            Rectangle(2, [1], 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(2, {52}, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(3, (1,2), 4, 5, 6)

    def test_width_getter(self):
        """Test the property of the width"""
        rect = Rectangle(2, 7, 1, 3, 9)
        self.assertEqual(2, rect.width)
        with self.assertRaises(ValueError):
            Rectangle(1, -2, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(4, 3.14, 7, 8, 1)
        with self.assertRaises(TypeError):
            Rectangle(6, "hello", 8, 7, 9)
        with self.assertRaises(TypeError):
            Rectangle([1], 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle({52}, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle((1,2), 3, 4, 5, 6)

    def test_height_setter(self):
        """Test the setter of the height"""
        rect = Rectangle(1, 12, 3, 15, 6)
        self.assertEqual(12, rect.height)
        with self.assertRaises(ValueError):
            Rectangle(1, -2, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(4, 3.14, 7, 8, 1)
        with self.assertRaises(TypeError):
            Rectangle(6, "hello", 8, 7, 9)
        with self.assertRaises(TypeError):
            Rectangle(2, [1], 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(2, {52}, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(3, (1,2), 4, 5, 6)

    def test_width_setter(self):
        """Test the setter of the width"""
        rect = Rectangle(4, 3, 2, 1, 9)
        self.assertEqual(4, rect.width)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(3.14, 6, 7, 8, 1)
        with self.assertRaises(TypeError):
            Rectangle("hello", 5, 8, 7, 9)
        with self.assertRaises(TypeError):
            Rectangle([1], 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle({52}, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle((1,2), 3, 4, 5, 6)


if __name__ == '__main__':
    unittest.main()
