#!/usr/bin/python3
"""test_base.py"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test case of the import class Base"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_id_is_None(self):
        """Test with id is None"""
        test1 = Base()
        self.assertEqual(test1.id, 1)
        test2 = Base()
        self.assertEqual(test2.id, 2)
        test3 = Base()
        self.assertEqual(test3.id, 3)

    def test_id_is_not_None(self):
        """Test with id=value"""
        test1 = Base()
        self.assertEqual(test1.id, 1)
        test2 = Base(5)
        self.assertEqual(test2.id, 5)
        test3 = Base(15)
        self.assertEqual(test3.id, 15)
        test4 = Base()
        self.assertEqual(test4.id, 2)

    def test_id_is_Zero(self):
        """Test with id is equal to Zero"""
        test1 = Base()
        self.assertEqual(test1.id, 1)
        test2 = Base(0)
        self.assertEqual(test2.id, 0)
        test3 = Base()
        self.assertEqual(test3.id, 2)
        test4 = Base()
        self.assertEqual(test4.id, 3)

    def test_id_is_positive(self):
        """Test if ID is positive"""
        test = Base(id=1)
        self.assertTrue(test.id > 0)

    def test_id_is_negative(self):
        """Test if ID is negative"""
        test = Base(id=-1)
        self.assertTrue(test.id < 0)

    def test_id_is_integer(self):
        """Test if ID is an integer"""
        test = Base(id="string")
        self.assertIsInstance(test.id, str)


if __name__ == '__main__':
    unittest.main()
