#!/usr/bin/python3
"""Unittest for the save_to_file and load_from_file methods"""

import unittest
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestLoadFile(unittest.TestCase):
    """Test case for the save_to_file and load_from_file methods"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    @classmethod
    def setUpClass(cls):
        """Set up the test environment"""
        cls.rectangle = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        cls.square = [Square(5), Square(7, 9, 1)]
        cls.rectangle_json = "Rectangle.json"
        cls.square_json= "Square.json"

    def test_save_and_load_rectangles(self):
        """Test save_to_file and load_from_file for rectangles"""
        Rectangle.save_to_file(self.rectangle)
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), len(self.rectangle))
        for loaded, original in zip(loaded_rectangles, self.rectangle):
            self.assertEqual(loaded.__dict__, original.__dict__)

    def test_save_and_load_squares(self):
        """Test save_to_file and load_from_file for squares"""
        Square.save_to_file(self.square)
        loaded_squares = Square.load_from_file()
        self.assertEqual(len(loaded_squares), len(self.square))
        for loaded, original in zip(loaded_squares, self.square):
            self.assertEqual(loaded.id, original.id)
            self.assertEqual(loaded.size, original.size)
            self.assertEqual(loaded.x, original.x)
            self.assertEqual(loaded.y, original.y)

    @classmethod
    def tearDownClass(cls):
        """Tear down the test environment"""
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
