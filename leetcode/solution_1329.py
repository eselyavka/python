#!/usr/bin/env python

import unittest


class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(mat)
        col = len(mat[0])
        seen = []
        for i in range(row):
            mas = []
            for j in range(col):
                mas.append(False)
            seen.append(mas)

        storage = dict()
        for i in range(row):
            buf = []
            for j in range(col):
                if seen[i][j]:
                    continue
                try:
                    r, c = i, j
                    while True:
                        seen[r][c] = True
                        buf.append(mat[r][c])
                        r += 1
                        c += 1
                except IndexError:
                    storage[i-j] = buf
                    buf = []

        for k in storage:
            if len(storage[k]) > 1:
                storage[k].sort(reverse=True)

        res = []
        for i in range(row):
            buf = []
            for j in range(col):
                diag = i - j
                val = storage[diag].pop()
                buf.append(val)
            res.append(buf)

        return res


class TestSolution(unittest.TestCase):

    def test_diagonalSort(self):
        solution = Solution()
        self.assertListEqual(solution.diagonalSort([[3, 3, 1, 1],
                                                    [2, 2, 1, 2],
                                                    [1, 1, 1, 2]]),
                             [[1, 1, 1, 1],
                              [1, 2, 2, 2],
                              [1, 2, 3, 3]])


if __name__ == '__main__':
    unittest.main()
