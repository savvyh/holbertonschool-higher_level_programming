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

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square"""
        s1 = Square(5)
        self.assertEqual(s1.to_dictionary(),
                         {'id': 1, 'size': 5, 'x': 0, 'y': 0})

        s2 = Square(3, 1, 3, 12)
        self.assertEqual(s2.to_dictionary(),
                         {'id': 12, 'size': 3, 'x': 1, 'y': 3})

    def test_to_dict_square_ok(self):
        """Test for dictionary for a normal square"""
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.to_dictionary(), {
                         'id': 1, 'x': 2, 'size': 10, 'y': 1})
        s1 = Square(10, 2, 1, 8)
        self.assertEqual(s1.to_dictionary(), {
                         'id': 8, 'x': 2, 'size': 10, 'y': 1})
        s5 = Square(3, 12)
        self.assertEqual(s5.to_dictionary(), {
                         'id': 2, 'x': 12, 'size': 3, 'y': 0})
        s6 = Square(3)
        self.assertEqual(s6.to_dictionary(), {
                         'id': 3, 'size': 3, 'x': 0, 'y': 0})

    def test_to_dict_square_value_error(self):
        """Test for value error of the square"""
        with self.assertRaises(ValueError):
            s2 = Square(-2, 3, 12)
            s2.to_dictionary()
        with self.assertRaises(ValueError):
            s3 = Square(2, -3, 12)
            s3.to_dictionary()
        with self.assertRaises(ValueError):
            s4 = Square(2, 3, -12)
            s4.to_dictionary()


if __name__ == '__main__':
    unittest.main()
