#!/usr/bin/env python

import unittest


class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(board)
        n = len(board[0])

        def adjacent_elements(board):
            s = set()

            for i in range(1, m - 1):
                for j in range(n):
                    if board[i - 1][j] == board[i][j] == board[i + 1][j] != 0:
                        s.add((i - 1, j))
                        s.add((i, j))
                        s.add((i + 1, j))

            for i in range(m):
                for j in range(1, n - 1):
                    if board[i][j - 1] == board[i][j] == board[i][j + 1] != 0:
                        s.add((i, j - 1))
                        s.add((i, j))
                        s.add((i, j + 1))
            return s

        res = adjacent_elements(board)
        while res:
            for i, j in res:
                board[i][j] = 0

            for j in range(n):
                i = m - 1
                while i != 0:
                    if i < m and board[i][j] == 0 and board[i - 1][j] != 0:
                        board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
                        i += 1
                        continue

                    i -= 1
            res = adjacent_elements(board)

        return board


class TestSolution(unittest.TestCase):

    def test_candyCrush(self):
        board = [[110, 5, 112, 113, 114],
                 [210, 211, 5, 213, 214],
                 [310, 311, 3, 313, 314],
                 [410, 411, 412, 5, 414],
                 [5, 1, 512, 3, 3],
                 [610, 4, 1, 613, 614],
                 [710, 1, 2, 713, 714],
                 [810, 1, 2, 1, 1],
                 [1, 1, 2, 2, 2],
                 [4, 1, 4, 4, 1014]]

        expected = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [110, 0, 0, 0, 114],
                    [210, 0, 0, 0, 214],
                    [310, 0, 0, 113, 314],
                    [410, 0, 0, 213, 414],
                    [610, 211, 112, 313, 614],
                    [710, 311, 412, 613, 714],
                    [810, 411, 512, 713, 1014]]
        solution = Solution()
        self.assertEqual(solution.candyCrush(board), expected)

if __name__ == '__main__':
    unittest.main()
