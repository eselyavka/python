#!/usr/bin/env python

import unittest


class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        need_change, res = '0', 0
        for c in target:
            if c != need_change:
                res += 1
                need_change = c

        return res


class TestSolution(unittest.TestCase):
    def test_minFlips(self):
        solution = Solution()
        self.assertEqual(solution.minFlips('101'), 3)


if __name__ == '__main__':
    unittest.main()
