"""
Validate if a given string is a numeric.
"""

import unittest

class Solution(object):
    """
    Class which implements validation
    """

    core_types = [int, float, long]

    def is_number(self, num_str, c_types=None):
        """
        :type num_str: str
        :type c_type: list
        :rtype: bool
        """

        if c_types is None:
            c_types = self.core_types

        if len(c_types) > 0:
            try:
                for c_type in c_types:
                    if (c_type((num_str.strip())) == 0 or
                        c_type(num_str.strip())): return True
            except ValueError:
                return self.is_number(num_str, c_types[c_types.index(c_type)+1:]) or False

class TestSolutionMethods(unittest.TestCase):
    """
    Test for Solution
    """

    def setUp(self):
        self.solution = Solution()

    def test_is_number(self):
        """
        Is string a number
        """
        self.assertTrue(self.solution.is_number("0"))
        self.assertTrue(self.solution.is_number(" 0.1 "))
        self.assertFalse(self.solution.is_number("abc"))
        self.assertFalse(self.solution.is_number("1 a"))
        self.assertTrue(self.solution.is_number("2e10"))

if __name__ == '__main__':
    unittest.main()
