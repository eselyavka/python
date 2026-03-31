#!/usr/bin/env python3

"""LeetCode solution 03043."""

import unittest


class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixes = set()

        for num in arr1:
            while num:
                prefixes.add(num)
                num //= 10

        ans = 0
        for num in arr2:
            while num:
                if num in prefixes:
                    ans = max(ans, len(str(num)))
                    break
                num //= 10

        return ans


class TestSolution(unittest.TestCase):
    def test_longestCommonPrefix(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix([1, 10, 100], [1000]), 3)
        self.assertEqual(solution.longestCommonPrefix([123, 12], [1299, 77]), 2)
        self.assertEqual(solution.longestCommonPrefix([5], [7]), 0)


if __name__ == '__main__':
    unittest.main()
