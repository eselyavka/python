#!/usr/bin/env python

import unittest

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])

        if row < 3 or column < 3:
            return 0

        def _check_number(digit, seen):
            if digit not in seen and 1 <= digit <= 9:
                return digit
            return None

        def is_magic(i, j):
            sum_rows, sum_columns, diag = [0] * 3
            seen_row, seen_column = set(), set()
            p = j

            for l in range(i, i+3):
                sum_columns = 0
                sum_rows = 0
                m = i
                for k in range(j, j+3):
                    row_element, col_element = (_check_number(grid[l][k], seen_row),
                                                _check_number(grid[m][p], seen_column))
                    if row_element is None or col_element is None:
                        return False

                    sum_rows += row_element
                    sum_columns += col_element

                    if l-i == k-j:
                        diag += row_element

                    seen_row.add(grid[l][k])
                    seen_column.add(grid[m][p])

                    m += 1

                p += 1

                if sum_rows != sum_columns:
                    return False

            return diag == sum_columns == sum_rows

        res = 0

        for i in range((row - 3)+1):
            for j in range((column - 3)+1):
                if is_magic(i, j):
                    res += 1

        return res

class TestSolution(unittest.TestCase):
    def test_numMagicSquaresInside(self):
        solution = Solution()

        grid = [[10, 3, 5],
                [1, 6, 11],
                [7, 9, 2]]
        actual = solution.numMagicSquaresInside(grid)
        self.assertEqual(actual, 0)

        grid = [[4, 3, 8, 4],
                [9, 5, 1, 9],
                [2, 7, 6, 2]]
        actual = solution.numMagicSquaresInside(grid)
        self.assertEqual(actual, 1)

        grid = [[2, 7, 6, 9],
                [9, 5, 1, 6],
                [4, 3, 8, 8],
                [1, 4, 10, 1]]
        actual = solution.numMagicSquaresInside(grid)
        self.assertEqual(actual, 1)

        grid = [[7, 0, 5],
                [2, 4, 6],
                [3, 8, 1]]
        actual = solution.numMagicSquaresInside(grid)
        self.assertEqual(actual, 0)

        grid = [[3, 2, 9, 2, 7],
                [6, 1, 8, 4, 2],
                [7, 5, 3, 2, 7],
                [2, 9, 4, 9, 6],
                [4, 3, 8, 2, 5]]
        actual = solution.numMagicSquaresInside(grid)
        self.assertEqual(actual, 1)

        grid = [[3, 10, 2, 3, 4],
                [4, 5, 6, 8, 1],
                [8, 8, 1, 6, 8],
                [1, 3, 5, 7, 1],
                [9, 4, 9, 2, 9]]
        actual = solution.numMagicSquaresInside(grid)
        self.assertEqual(actual, 1)

        grid = [[8, 9, 4, 8, 7, 7, 3, 4, 3, 6],
                [1, 9, 9, 2, 4, 9, 3, 8, 4, 7],
                [2, 4, 8, 9, 4, 1, 5, 6, 8, 2],
                [8, 8, 2, 4, 2, 5, 6, 1, 4, 9],
                [8, 2, 6, 8, 8, 4, 4, 5, 4, 1],
                [8, 2, 6, 3, 5, 2, 3, 8, 7, 1],
                [8, 1, 6, 7, 5, 2, 5, 6, 8, 9],
                [4, 6, 4, 4, 7, 4, 6, 2, 6, 4],
                [3, 7, 9, 8, 2, 8, 9, 1, 8, 5],
                [1, 8, 6, 2, 1, 7, 3, 3, 7, 9]]

        actual = solution.numMagicSquaresInside(grid)
        self.assertEqual(actual, 0)

if __name__ == '__main__':
    unittest.main()
