#!/usr/bin/python3
"""test_rectangle.py"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):
    """Test case of the import class Base"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_without_id(self):
        """Test without the ID but with width, height, x or y"""
        test1 = Rectangle(8, 3)
        self.assertEqual(test1.id, 1)
        test2 = Rectangle(1, 5, 4)
        self.assertEqual(test2.id, 2)
        test3 = Rectangle(6, 7, 1, 6)
        self.assertEqual(test3.id, 3)

    def test_with_id(self):
        """Test with an ID"""
        test = Rectangle(1, 8, 9, 4, 25)
        self.assertEqual(test.id, 25)

    def test_id_is_positive(self):
        """Test with a positive ID"""
        test = Rectangle(2, 6, 0, 0, 5)
        self.assertTrue(test.id > 0)

    def test_id_is_negative(self):
        """Test if ID is negative"""
        test = Rectangle(2, 5, 8, 0, -2)
        self.assertTrue(test.id < 0)

    def test_id_is_integer(self):
        """Test if ID is an integer"""
        test = Rectangle(1, 5, 74, 0, "hello")
        self.assertIsInstance(test.id, str)


if __name__ == '__main__':
    unittest.main()
