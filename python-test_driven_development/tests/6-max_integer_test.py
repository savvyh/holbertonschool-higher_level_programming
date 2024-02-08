#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_success(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1, 3, 3, 3, 6, 8, 8]), 8)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 2, 3, 4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_is_none(self):
        """test if argument is None"""
        self.assertIsNone(max_integer())

    def test_non_int(self):
        """test if one argument is not an int"""
        self.assertRaises(TypeError, max_integer, ["Holberton", 3.14, 97, 8])

    def test_mixed_list(self):
        """test with a list of mixed data types"""
        self.assertRaises(TypeError, max_integer, ["a", "b", 1])
