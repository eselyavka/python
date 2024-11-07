#!/usr/bin/env python

import unittest


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        res = []
        if n % 2 == 1:
            res.append(0)

        i = 1
        while len(res) != n:
            res.append(i)
            i = -i if i > 0 else ((i*-1)+1)

        return res


class TestSolution(unittest.TestCase):
    def test_sumZero(self):
        solution = Solution()
        self.assertListEqual(sorted(solution.sumZero(5)), sorted([-1, 1, 2, 0, -2]))


if __name__ == '__main__':
    unittest.main()
