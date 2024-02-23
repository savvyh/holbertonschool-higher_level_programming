#!/usr/bin/python3
"""Unittest for Square class"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test case for Square class"""

    def test_init(self):
        """Test initialization"""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 2)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s = Square(5, 2, 3, 10)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, {'id': 10, 'size': 5, 'x': 2, 'y': 3})

    def test_update(self):
        """Test update method"""
        s = Square(5, 2, 3, 10)
        s.update(20, 10, 5, 1)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 1)

    def test_str(self):
        """Test __str__ method"""
        s = Square(5, 2, 3, 10)
        self.assertEqual(str(s), '[Square] (10) 2/3 - 5')


if __name__ == '__main__':
    unittest.main()
