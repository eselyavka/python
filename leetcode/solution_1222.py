#!/usr/bin/python

import unittest


class Solution(object):
    def gen_horizontal(self, row, col, s, king):
        left = False
        right = False

        for i in range(col - 1, -1, -1):
            if (row, i) in s:
                break
            if [row, i] == king:
                left = True
                break

        for i in range(col + 1, 8):
            if (row, i) in s:
                break
            if [row, i] == king:
                right = True
                break

        return any([left, right])

    def gen_vertical(self, row, col, s, king):
        up = False
        down = False

        for i in range(row - 1, -1, -1):
            if (i, col) in s:
                break
            if [i, col] == king:
                up = True
                break

        for i in range(row + 1, 8):
            if (i, col) in s:
                break
            if [i, col] == king:
                down = True
                break

        return any([up, down])

    def gen_diagonal(self, i, j, s, king):
        diag1_up, diag1_down, diag2_up, diag2_down = [False] * 4

        row = i
        col = j
        while col < 8 or row < 8:
            col += 1
            row += 1
            if (row, col) in s:
                break
            if [row, col] == king:
                diag1_down = True
                break

        row = i
        col = j
        while col >= 0 or row >= 0:
            col -= 1
            row -= 1
            if (row, col) in s:
                break
            if [row, col] == king:
                diag1_up = True
                break

        row = i
        col = j
        while col >= 0 or row < 8:
            col -= 1
            row += 1
            if (row, col) in s:
                break
            if [row, col] == king:
                diag2_down = True
                break

        row = i
        col = j
        while col < 8 or row >= 0:
            col += 1
            row -= 1
            if (row, col) in s:
                break
            if [row, col] == king:
                diag2_up = True
                break

        return any([diag1_up, diag1_down, diag2_up, diag2_down])

    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queens_set = set([tuple(x) for x in queens])
        res = []

        for q in queens:
            row, col = q

            if self.gen_horizontal(row, col, queens_set, king):
                res.append(q)

            if self.gen_vertical(row, col, queens_set, king):
                res.append(q)

            if self.gen_diagonal(row, col, queens_set, king):
                res.append(q)

        return res


class TestSolution(unittest.TestCase):

    def test_queensAttacktheKing(self):
        solution = Solution()
        self.assertListEqual(solution.queensAttacktheKing([[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], [0, 0]), [[0, 1], [1, 0], [3, 3]])


if __name__ == '__main__':
    unittest.main()
