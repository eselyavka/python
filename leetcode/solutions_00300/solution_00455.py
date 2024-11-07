#!/usr/bin/env python

import unittest


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res, i, j = 0, 0, 0
        g.sort()
        s.sort()
        while True:
            if i >= len(g):
                break
            if j >= len(s):
                break
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1

        return res


class TestSolution(unittest.TestCase):
    def test_findContentChildren(self):
        solution = Solution()
        self.assertEqual(solution.findContentChildren([1, 2, 3], [1, 1]), 1)
        self.assertEqual(solution.findContentChildren([1, 2], [1, 2, 3]), 2)
        self.assertEqual(solution.findContentChildren([1, 2, 3], [1, 1, 1]), 1)
        self.assertEqual(solution.findContentChildren([1, 2, 3], [3]), 1)
        self.assertEqual(solution.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]), 2)


if __name__ == '__main__':
    unittest.main()
