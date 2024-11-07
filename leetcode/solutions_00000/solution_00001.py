#!/usr/bin/env python

import unittest

class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for i, number in enumerate(numbers):
            if number in d:
                return [d[number]+1, i+1]
            else:
                d[target - number] = i

class TestSolution(unittest.TestCase):

    def test_twoSum(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(solution.twoSum([2, 3, 4], 6), [1, 3])

if __name__ == '__main__':
    unittest.main()
