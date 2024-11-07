#!/usr/bin/env python

import unittest


class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        n = len(rowSum)
        m = len(colSum)
        res = []

        for i in range(n):
            row_target = rowSum[i]
            buf = []
            for j in range(m):
                if row_target > colSum[j]:
                    buf.append(colSum[j])
                    row_target -= colSum[j]
                    colSum[j] = 0
                else:
                    buf.append(row_target)
                    colSum[j] -= row_target
                    row_target = 0
            res.append(buf)

        return res


class TestSolution(unittest.TestCase):
    def test_restoreMatrix(self):
        solution = Solution()
        self.assertEqual(solution.restoreMatrix([3, 8], [4, 7]), [[3, 0], [1, 7]])


if __name__ == '__main__':
    unittest.main()
