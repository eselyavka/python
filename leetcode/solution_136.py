#!/usr/bin/env python

import unittest


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        res = 0
        for num in nums:
            res ^= num

        return res


class TestSolution(unittest.TestCase):

    def test_singleNumber(self):
        solution = Solution()
        self.assertEqual(solution.singleNumber([2, 2, 1]), 1)


if __name__ == '__main__':
    unittest.main()
