#!/usr/bin/env python

import unittest

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()

        def rec(i, j):
            if i == j:
                res.append(nums[:])
            else:
                for k in range(i, j + 1):
                    nums[i], nums[k] = nums[k], nums[i]
                    rec(i+1, j)
                    nums[i], nums[k] = nums[k], nums[i]

        rec(0, len(nums) - 1)

        return res

class TestSolution(unittest.TestCase):

    def test_permutate(self):
        nums = [1, 2, 3]
        solution = Solution()
        self.assertEqual(solution.permute(nums), [[1, 2, 3],
                                                  [1, 3, 2],
                                                  [2, 1, 3],
                                                  [2, 3, 1],
                                                  [3, 2, 1],
                                                  [3, 1, 2]])

if __name__ == '__main__':
    unittest.main()
