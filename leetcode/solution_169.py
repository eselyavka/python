#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)

        majority = len(nums)//2

        for num in nums:
            d[num] += 1

            if d[num] > majority:
                return num

class TestSolution(unittest.TestCase):
    def test_majorityElement(self):
        solution = Solution()
        self.assertEqual(solution.majorityElement([3, 2, 3]), 3)
        self.assertEqual(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

if __name__ == '__main__':
    unittest.main()
