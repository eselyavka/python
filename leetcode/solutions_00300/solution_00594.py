#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return 0

        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        _max = 0

        for num in nums:
            res = d[num + 1] if num + 1 in d else 0
            res += d[num] if num in d and res else 0
            _max = max(_max, res)

        return _max

class TestSolution(unittest.TestCase):
    def test_findLHS(self):
        solution = Solution()
        self.assertEqual(solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]), 5)


if __name__ == '__main__':
    unittest.main()
