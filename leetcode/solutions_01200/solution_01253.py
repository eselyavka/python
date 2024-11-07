#!/usr/bin/env python

import unittest


class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n = 2
        m = len(colsum)
        rows = [upper, lower]
        res = [[None for _ in range(m)] for _ in range(n)]

        for j, c in enumerate(colsum):
            if c == 0:
                res[0][j] = 0
                res[1][j] = 0
            elif c == 2:
                res[0][j] = 1
                res[1][j] = 1
                rows[0] -= 1
                rows[1] -= 1

        if rows[0] < 0 or rows[1] < 0:
            return []

        for j, c in enumerate(colsum):
            if c != 1:
                continue
            if rows[0] > 0:
                res[0][j] = 1
                rows[0] -= 1
            else:
                res[0][j] = 0

            if rows[1] > 0:
                if res[0][j] == 1:
                    res[1][j] = 0
                else:
                    res[1][j] = 1
                    rows[1] -= 1
            else:
                if res[0][j] == 0:
                    return []
                res[1][j] = 0

        return [] if any(rows) else res


class TestSolution(unittest.TestCase):
    def test_reconstructMatrix(self):
        solution = Solution()
        self.assertEqual(solution.reconstructMatrix(2, 1, [1, 1, 1]), [[1, 1, 0],
                                                                       [0, 0, 1]])


if __name__ == '__main__':
    unittest.main()
