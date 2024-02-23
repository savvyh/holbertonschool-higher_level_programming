#!/usr/bin/python3
"""test_rectangle.py"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test case of the import class Rectangle"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_without_id(self):
        """Test without the ID but without width, height, x or y"""
        test1 = Rectangle(8, 3)
        self.assertEqual(test1.id, 1)
        test2 = Rectangle(1, 5, 4)
        self.assertEqual(test2.id, 2)
        test3 = Rectangle(6, 7, 1, 6)
        self.assertEqual(test3.id, 3)

    def test_id(self):
        """Test with ID assignments"""
        test = Rectangle(1, 8, 9, 4, 25)
        self.assertEqual(test.id, 25)
        test = Rectangle(2, 6, 0, 0, 5)
        self.assertTrue(test.id > 0)
        test = Rectangle(2, 5, 8, 0, -2)
        self.assertTrue(test.id < 0)
        test_string = Rectangle(1, 2, 3, 4, "hello")
        self.assertIsInstance(test_string.id, str)

    def test_x_setter(self):
        """Test with x assignments"""
        rect = Rectangle(10, 6, 5, 0, 1)
        self.assertEqual(5, rect.x)
        with self.assertRaises(ValueError):
            Rectangle(6, 2, -8, 9, 1)
        with self.assertRaises(TypeError):
            Rectangle(6, 2, 1.35, 9, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 7, "hello", 0, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 7, None, 0, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 7, (1, 2), 0, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 7, [12], 0, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 7, {4}, 0, 1)

    def test_y_setter(self):
        """Test with y assignments"""
        rect = Rectangle(10, 6, 0, 5, 1)
        self.assertEqual(5, rect.y)
        with self.assertRaises(ValueError):
            Rectangle(6, 2, 8, -9, 1)
        with self.assertRaises(TypeError):
            Rectangle(6, 2, 1, 1.35, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 7, 0, "hello", 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 7, 0, None, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 7, 0, (1, 2), 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 7, 0, [12], 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 7, 0, {4}, 1)

    def test_x_getter(self):
        """Test the x getter"""
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(4, rect.x)

    def test_y_getter(self):
        """Test the y getter"""
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(5, rect.y)

    def test_rectangle_assignments(self):
        """Test rectangle assignments"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {"age": 27}, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, [1, 2], 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, (1, 2), 5)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4, 8)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "hello", 9)
        with self.assertRaises(TypeError):
            Rectangle(None, None, None, None)


if __name__ == '__main__':
    unittest.main()
