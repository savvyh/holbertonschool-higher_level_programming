#!/usr/bin/python3
"""test_square_area.py"""

import unittest
from models.square import Square
from models.base import Base


class TestSquareToDictionary(unittest.TestCase):
    """Test the dictionnary of the class Square"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_area(self):
        """Test the area method of Square"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(7, 0, 0, 12)
        self.assertEqual(s2.area(), 49)
