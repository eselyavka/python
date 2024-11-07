#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tmp_sum = 0
        res = 0
        d = defaultdict(int)

        for num in nums:
            tmp_sum += num

            if tmp_sum == k:
                res += 1

            if tmp_sum - k in d:
                res += d[tmp_sum - k]

            d[tmp_sum] += 1

        return res

class TestSolution(unittest.TestCase):
    def test_subarraySum(self):
        solution = Solution()
        self.assertEquals(solution.subarraySum([1, 1, 1], 2), 2)
        self.assertEquals(solution.subarraySum([28, 54, 7, -70, 22, 65, -6], 100), 1)
        self.assertEquals(solution.subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0), 55)

if __name__ == '__main__':
    unittest.main()
