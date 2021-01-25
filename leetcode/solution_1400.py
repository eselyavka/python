#!/usr/bin/env python

import unittest
from collections import Counter


class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False

        cnt = Counter(s)
        odd = 0

        for _, num in cnt.items():
            if num % 2 == 1:
                odd += 1
            if odd > k:
                return False

        return True


class TestSolution(unittest.TestCase):
    def test_canConstruct(self):
        solution = Solution()
        self.assertTrue(solution.canConstruct('annabelle', 2))


if __name__ == '__main__':
    unittest.main()
