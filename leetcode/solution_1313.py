#!/usr/bin/env python

import unittest


class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for i in range(1, len(nums), 2):
            for _ in range(nums[i-1]):
                res.append(nums[i])

        return res


class TestSolution(unittest.TestCase):

    def test_decompressRLElist(self):
        solution = Solution()
        self.assertListEqual(
            solution.decompressRLElist([1, 2, 3, 4]),
            [2, 4, 4, 4])


if __name__ == '__main__':
    unittest.main()
