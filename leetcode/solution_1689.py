#!/usr/bin/env python

import unittest


class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        return int(max(list(n)))


class TestSolution(unittest.TestCase):
    def test_minPartitions(self):
        solution = Solution()
        self.assertEqual(solution.minPartitions('32'), 3)


if __name__ == '__main__':
    unittest.main()
