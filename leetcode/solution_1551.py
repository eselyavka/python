#!/usr/bin/env python

import unittest


class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [i*2+1 for i in range(n)]
        target = sum(arr) / n
        res = sum(set([abs(target - x) for x in arr]))

        return res


class TestSolution(unittest.TestCase):
    def test_minOperations(self):
        solution = Solution()
        self.assertEqual(solution.minOperations(3), 2)


if __name__ == '__main__':
    unittest.main()
