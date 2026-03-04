#!/usr/bin/env python3

"""LeetCode solution 01582."""

import unittest


class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = len(mat)
        cols = len(mat[0])

        row_counts = [0] * rows
        col_counts = [0] * cols

        for row_idx in range(rows):
            for col_idx in range(cols):
                if mat[row_idx][col_idx] == 1:
                    row_counts[row_idx] += 1
                    col_counts[col_idx] += 1

        special = 0
        for row_idx in range(rows):
            if row_counts[row_idx] != 1:
                continue

            for col_idx in range(cols):
                if mat[row_idx][col_idx] == 1 and col_counts[col_idx] == 1:
                    special += 1

        return special


class TestSolution(unittest.TestCase):
    def test_numSpecial(self):
        solution = Solution()
        self.assertEqual(solution.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]), 1)


if __name__ == '__main__':
    unittest.main()
