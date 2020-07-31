#!/usr/bin/env python

import unittest


class Solution(object):
    def __init__(self):
        self.cnt = 0
        self.res = ''

    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr = ['a', 'b', 'c']

        def rec(arr, target, curr, n, k):
            if len(target) == n:
                if self.cnt == k-1:
                    self.res = target
                self.cnt += 1
                return
            for c in arr:
                if c == curr:
                    continue
                rec(arr, target + c, c, n, k)

        rec(arr, '', '', n, k)

        return self.res


class TestSolution(unittest.TestCase):
    def test_getHappyString(self):
        solution = Solution()
        self.assertEqual(solution.getHappyString(3, 9), 'cab')


if __name__ == '__main__':
    unittest.main()
