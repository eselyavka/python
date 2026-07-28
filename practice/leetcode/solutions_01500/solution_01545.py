#!/usr/bin/env python3

"""LeetCode solution 01545."""

import unittest


class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        current = "0"

        for _ in range(2, n + 1):
            right = ''.join('1' if char == '0' else '0' for char in reversed(current))
            current = current + "1" + right

        return current[k - 1]


class TestSolution(unittest.TestCase):
    def test_findKthBit(self):
        solution = Solution()
        self.assertEqual(solution.findKthBit(3, 1), '0')
        self.assertEqual(solution.findKthBit(4, 11), '1')
        self.assertEqual(solution.findKthBit(1, 1), '0')
        self.assertEqual(solution.findKthBit(2, 3), '1')


if __name__ == '__main__':
    unittest.main()
