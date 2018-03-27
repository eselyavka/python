"""
Find 2nd largest element in array
"""

import unittest

class Solution(object):
    """
    Class which implements algorithm
    """
    def secondLargestElement(self, array):
        _max = _prev = float('-inf')

        for num in array:
            if _max < num:
                _prev = _max
                _max = num
            elif num < _max and num > _prev:
                _prev = num

        return _prev if _prev != float('-inf') else None

class TestSolutionMethods(unittest.TestCase):
    """
    Test for Solution
    """

    def setUp(self):
        self.solution = Solution()

    def test_is_number(self):
        """
        Find 2nd largest element in array
        """
        self.assertEqual(self.solution.secondLargestElement([12, 35, 1, 10, 34, 1]), 34)
        self.assertEqual(self.solution.secondLargestElement([10, 5, 10]), 5)
        self.assertIsNone(self.solution.secondLargestElement([10, 10, 10]))

if __name__ == '__main__':
    unittest.main()
