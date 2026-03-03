#!/usr/bin/env python3

"""LeetCode solution 01492."""

import unittest


class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factor = [1]
        for i in range(2, n+1):
            if n % i == 0:
                factor.append(i)

        try:
            return factor[k-1]
        except IndexError:
            pass

        return -1


class TestSolution(unittest.TestCase):
    def test_kthFactor(self):
        solution = Solution()
        self.assertEqual(solution.kthFactor(12, 3), 3)


if __name__ == '__main__':
    unittest.main()
