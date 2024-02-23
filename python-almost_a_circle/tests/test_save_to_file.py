#!/usr/bin/python3
"""Unittest for the save_to_file method in Rectangle class"""

import unittest
import os
from models.rectangle import Rectangle


class TestSaveToFile(unittest.TestCase):
    """Test case for the save_to_file method in Rectangle class"""

    def setUp(self):
        """Reset the file content before each test"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            file_content = file.read()
            self.assertIn('"width": 10', file_content)
            self.assertIn('"height": 7', file_content)
            self.assertIn('"x": 2', file_content)
            self.assertIn('"y": 8', file_content)
            self.assertIn('"width": 2', file_content)
            self.assertIn('"height": 4', file_content)
            self.assertIn('"x": 0', file_content)
            self.assertIn('"y": 0', file_content)


if __name__ == '__main__':
    unittest.main()
