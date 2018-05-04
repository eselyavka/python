#!/usr/bin/env python

import unittest

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        size = 2**len(nums)
        res = []
        for i in range(size):
            tmp = []
            for j in range(len(nums)):
                if i & (1<<j):
                    tmp.append(nums[j])
            res.append(tmp)

        return res

class TestSolution(unittest.TestCase):

    def test_subsets(self):
        solution = Solution()
        self.assertEqual(solution.subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3],
                                                       [1, 3], [2, 3], [1, 2, 3]])
        self.assertEqual(solution.subsets([1, 2]), [[], [1], [2], [1, 2]])
        self.assertEqual(solution.subsets([0]), [[], [0]])

if __name__ == '__main__':
    unittest.main()
