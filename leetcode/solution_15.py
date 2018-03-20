#!/usr/bin/env python

import unittest

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        n = len(nums)
        res = set()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return [list(x) for x in res]

class TestSolution(unittest.TestCase):

    def test_threeSum(self):
        solution = Solution()
        self.assertEqual(solution.threeSum([-1, 0, 1, 2, -1, -4]),
                         [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(solution.threeSum([1, 1, -2]), [[-2, 1, 1]])
        self.assertEqual(solution.threeSum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(solution.threeSum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])

if __name__ == '__main__':
    unittest.main()
