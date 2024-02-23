#!/usr/bin/python3
"""Unittest for create method in Rectangle class"""

import unittest
from models.rectangle import Rectangle


class TestCreateMethod(unittest.TestCase):
    """Test case for create method in Rectangle class"""

    def test_create_method(self):
        """Test create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertIsNotNone(r2)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertIsNot(r1, r2)


if __name__ == '__main__':
    unittest.main()
