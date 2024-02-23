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

    def test_id_is_integer(self):
        """Test if ID is an integer"""
        test = Square(1, 74, 0, "hello")
        self.assertIsInstance(test.id, str)

    def test_square(self):
        """Test with size"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)

    def test_square_x(self):
        """Test with a size and a x"""
        s1 = Square(2, 2)
        self.assertEqual(str(s1), "[Square] (1) 2/0 - 2")
        self.assertEqual(s1.area(), 4)

    def test_square_x_y(self):
        """Test with a size, x and y"""
        s1 = Square(3, 1, 3)
        self.assertEqual(str(s1), "[Square] (1) 1/3 - 3")
        self.assertEqual(s1.area(), 9)

    def test_str_method(self):
        """Test __str__ method"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

    def test_update_method(self):
        """Test update method"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_x_typeerror(self):
        """Test x is not int"""
        with self.assertRaises(TypeError):
            Square("hello")

    def test_y_typeerror(self):
        """Test y is not int"""
        with self.assertRaises(TypeError):
            Square(1, "hello")

    def test_size_valueerror(self):
        """Test size <= 0"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_valueerror(self):
        """Test x <= 0"""
        with self.assertRaises(ValueError):
            Square(1, -1)

    def test_y_valueerror(self):
        """Test y <= 0"""
        with self.assertRaises(ValueError):
            Square(1, 1, -1)


if __name__ == '__main__':
    unittest.main()
