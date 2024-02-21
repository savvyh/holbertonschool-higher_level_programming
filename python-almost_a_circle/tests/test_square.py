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

    def test_without_id(self):
        """Test without the ID but with others attributes"""
        test = Square(8, 3)
        self.assertEqual(test.id, 1)

    def test_with_id(self):
        """Test with an ID"""
        test = Square(1, 9, 4, 25)
        self.assertEqual(test.id, 25)

    def test_id_is_negative(self):
        """Test if ID is negative"""
        test = Square(2, 8, 0, -2)
        self.assertTrue(test.id < 0)
