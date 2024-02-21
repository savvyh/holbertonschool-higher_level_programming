#!/usr/bin/python3
"""test_square.py"""

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test Case of the import class Square"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_size_setter(self):
        """Test the setter of the size"""
        test = Square(4, 3, 1, 9)
        self.assertEqual(4, test.size)

    def test_size_setter_negative(self):
        """Test to set a negative int to the size"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 4, 5)

if __name__ == '__main__':
    unittest.main()
