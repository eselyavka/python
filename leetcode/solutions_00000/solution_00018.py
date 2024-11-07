#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def is_diff(self, t1, t2):
        if (t1[0] == t2[0] or
                t1[0] == t2[1] or
                t1[1] == t2[0] or
                t1[1] == t2[1]):
            return False

        return True

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(nums)
        d = defaultdict(list)
        s = set()

        for i in range(size):
            for j in range(i+1, size):
                _sum = nums[i]+nums[j]
                idx = target - _sum
                if d.has_key(idx):
                    for t in d[idx]:
                        if self.is_diff(t, (i, j)):
                            s.add(tuple(sorted([nums[t[0]], nums[t[1]], nums[i], nums[j]])))
                    d[_sum] += [(i, j)]
                d[_sum] += [(i, j)]

        return [list(x) for x in s]

class TestSolution(unittest.TestCase):

    def test_fourSum(self):
        solution = Solution()
        self.assertEqual(solution.fourSum([1, 0, -1, 0, -2, 2], 0),
                         [[-1, 0, 0, 1],
                          [-2, -1, 1, 2],
                          [-2, 0, 0, 2]])
        self.assertEqual(len(solution.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)), 8)

if __name__ == '__main__':
    unittest.main()
