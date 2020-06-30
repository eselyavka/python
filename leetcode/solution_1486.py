#!/usr/bin/env python

import unittest


class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        i, res = 0, 0
        while i < n:
            res ^= start + 2 * i
            i += 1

        return res


class TestSolution(unittest.TestCase):
    def test_xorOperation(self):
        solution = Solution()
        self.assertEqual(solution.xorOperation(5, 0), 8)


if __name__ == '__main__':
    unittest.main()
