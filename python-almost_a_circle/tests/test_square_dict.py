#!/usr/bin/python3
"""test_square_dict.py"""

import unittest
from models.square import Square
from models.base import Base


class TestSquareToDictionary(unittest.TestCase):
    """Test the dictionnary of the class Square"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_to_dictionary_with_float(self):
        """Test with a float"""
        s = Square(5, 5, 5)
        with self.assertRaises(TypeError):
            s.x = 5.5

    def test_to_dictionary_with_list(self):
        """Test with a list inside the dict"""
        s = Square(5, 5, 5)
        with self.assertRaises(TypeError):
            s.y = [1, 2, 3]

    def test_to_dictionary_with_tuple(self):
        """Test with a tuple inside the dict"""
        s = Square(5, 5, 5)
        with self.assertRaises(TypeError):
            s.size = (1, 2)

    def test_to_dictionary_with_none(self):
        """Test with a None inside the dict"""
        s = Square(5, 5, 5)
        with self.assertRaises(TypeError):
            s.size = None


if __name__ == '__main__':
    unittest.main()
