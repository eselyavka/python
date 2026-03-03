#!/usr/bin/env python3

"""LeetCode solution 00561."""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sum(sorted(nums)[::2])
