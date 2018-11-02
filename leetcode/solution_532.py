#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        s = set()
        nums_s = defaultdict(int)
        for num in nums:
            nums_s[num] += 1
        for num in nums:
            if num == num - k and num - k in nums_s and nums_s[num-k] == 1:
                continue
            if num - k in nums_s:
                s.add((num, num - k))
                nums_s[num-k] -= 1

        return len(s)

class TestSolution(unittest.TestCase):
    def test_findPairs(self):
        solution = Solution()
        self.assertEqual(solution.findPairs([3, 1, 4, 1, 5], 2), 2)
        self.assertEqual(solution.findPairs([3, 1, 4, 1, 5], 2), 2)
        self.assertEqual(solution.findPairs([1, 2, 3, 4, 5], -1), 0)
        self.assertEqual(solution.findPairs([1, 2, 3, 4, 5], 1), 4)
        self.assertEqual(solution.findPairs([1, 3, 1, 5, 4], 0), 1)

if __name__ == '__main__':
    unittest.main()
