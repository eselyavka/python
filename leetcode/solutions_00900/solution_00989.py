#!/usr/bin/env python

import unittest


class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        M, pow_ = 0, 0
        while A:
            M += A.pop() * (10**pow_)
            pow_ += 1
        _res = M + K

        if not _res:
            return [0]

        while _res:
            A.append(_res % 10)
            _res = _res // 10

        return A[::-1]


class TestSolution(unittest.TestCase):
    def test_addToArrayForm(self):
        solution = Solution()
        self.assertTrue(solution.addToArrayForm([1, 2, 0, 0], 34), [1, 2, 3, 4])
        self.assertTrue(solution.addToArrayForm([2, 7, 4], 181), [4, 5, 5])


if __name__ == '__main__':
    unittest.main()
