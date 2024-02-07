#!/usr/bin/python3
"""
Unittests for the function max_integer(list=[])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Defines TextMaxInteger class
    """

    def test_ordered_list(self):
        """
        Test an orderd list of integers
        """
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """
        Test an unordered list of integers
        """
        unordered = [2, 1, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """
        Test a list with max value at the beginning
        """
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """
        Test an empty list
        """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        """
        Test a list with one element
        """
        one_element = [4]
        self.assertEqual(max_integer(one_element), 4)

    def test_floats(self):
        """
        Test a list with floats
        """
        floats = [-1.34, 0.6, 3.8, -12.89, 7.77]
        self.assertEqual(max_integer(floats), 7.77)

    def test_ints_and_floats(self):
        """
        Test a list with integers and floats
        """
        ints_and_floats = [1.3, -4, 3.14, 7, -5.73, 2]
        self.assertEqual(max_integer(ints_and_floats), 7)

    def test_string(self):
        """
        Test a string
        """
        string = "rain"
        self.assertEqual(max_integer(string), "r")

    def test_none_is_arg(self):
        """
        Test if None is supplied as an argument
        """
        self.assertRaises(TypeError, max_integer, None)

    def test_wrong_type_in_list(self):
        """
        Test a list with a wrong type
        """
        wrong_type = [1, 0, -3, 4.34, "Alx", -2.7]
        self.assertRaises(TypeError, max_integer, wrong_type)

    def test_no_args(self):
        """
        Test if no argument was supplied
        """
        self.assertIsNone(max_integer())


if __name__ == "__main__":
    unittest.main()


