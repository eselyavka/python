#!/usr/bin/env python

import unittest

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        res = 0
        vector = [0] * 32
        for num in nums:
            i = 0
            while num > 0:
                vector[i] += num & 0x1
                num >>= 1
                i += 1

        for i in vector:
            res += i * (size - i)

        return res

class TestSolution(unittest.TestCase):
    def test_totalHammingDistance(self):
        solution = Solution()
        self.assertEqual(solution.totalHammingDistance([4, 14, 2]), 6)

if __name__ == '__main__':
    unittest.main()
