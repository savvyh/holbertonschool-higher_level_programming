#!/usr/bin/python3
"""test_base.py"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test case of the import class Base"""

    def setUp(self):
        """Reset the variable __nb_objects for each test"""
        Base._Base__nb_objects = 0

    def test_without_id(self):
        """Test without id"""
        test1 = Base()
        self.assertEqual(test1.id, 1)

    def test_with_id(self):
        """Test with a specific ID"""
        test2 = Base(12)
        self.assertEqual(test2.id, 12)

    def test_with_negative_id(self):
        """Test with a negative ID"""
        test3 = Base(-8)
        self.assertEqual(test3.id, -8)

    def test_with_float_id(self):
        """Test with a float ID"""
        test4 = Base(6.3)
        self.assertEqual(test4.id, 6.3)

    def test_without_id_after_others(self):
        """Test without id (after other instantiations)"""
        test5 = Base()
        self.assertEqual(test5.id, 1)

    def test_with_none_id(self):
        """Test with None as ID"""
        test6 = Base(None)
        self.assertEqual(test6.id, 1)

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty(self):
        """Test to_json_string with non-empty list"""
        input_list = [{"key": "value"}, {"key2": "value2"}]
        result = Base.to_json_string(input_list)
        self.assertEqual(result, '[{"key": "value"}, {"key2": "value2"}]')

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string"""
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty(self):
        """Test from_json_string with non-empty string"""
        input_string = '[{"key": "value"}, {"key2": "value2"}]'
        result = Base.from_json_string(input_string)
        expected_result = [{"key": "value"}, {"key2": "value2"}]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
