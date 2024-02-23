#!/usr/bin/python3
"""Unittest for Rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleUpdate(unittest.TestCase):
    """Test case for Rectangle update method"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_update(self):
        """Test update method"""
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/1 - 1/1")

        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/1 - 1/1")

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/1 - 2/1")

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/1 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/1 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")


if __name__ == '__main__':
    unittest.main()
