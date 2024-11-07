#!/usr/bin/env python

import unittest

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])

        parentheses_open = '(' if len(nums[1:]) > 1 else ''
        parentheses_close = ')' if len(nums[1:]) > 1 else ''

        return (str(nums[0]) + '/' +
                parentheses_open +
                '/'.join([str(x) for x in nums[1:]]) +
                parentheses_close)

class TestSolution(unittest.TestCase):

    def test_optimalDivision(self):
        solution = Solution()
        self.assertEqual(solution.optimalDivision([1000, 100, 10, 2]), "1000/(100/10/2)")
        self.assertEqual(solution.optimalDivision([2, 3, 4]), "2/(3/4)")
        self.assertEqual(solution.optimalDivision([2]), "2")
        self.assertEqual(solution.optimalDivision([3, 2]), "3/2")

if __name__ == '__main__':
    unittest.main()
