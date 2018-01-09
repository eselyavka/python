#!/usr/bin/env python

import unittest

class Solution(object):
    def get_crashing_elements(self, board):
        elements = set()

        for i in range(len(board)):
            for j in range(len(board[i])):
                element = board[i][j]

                if element == 0:
                    continue

                if (j - 1 >= 0 and j + 1 < len(board[i]) and
                        board[i][j - 1] == element and board[i][j + 1] == element or
                        j - 2 >= 0 and board[i][j - 1] == element and board[i][j - 2] == element or
                        j + 2 <= len(board[i]) - 1 and board[i][j + 1] == element and
                        board[i][j + 2] == element or
                        i - 1 >= 0 and i + 1 < len(board) and board[i - 1][j] == element and
                        board[i + 1][j] == element or
                        i - 2 >= 0 and board[i - 1][j] == element and board[i - 2][j] == element or
                        i + 2 <= len(board) - 1 and board[i + 1][j] == element and
                        board[i + 2][j] == element):
                    elements.add((i, j))
        return elements

    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """

        elements = self.get_crashing_elements(board)

        while elements:
            for row, col in elements:
                board[row][col] = 0

            for j in range(len(board[0])):
                i = len(board) - 1
                while i != 0:
                    if i < len(board) and board[i][j] == 0 and board[i-1][j] != 0:
                        buf = board[i-1][j]
                        board[i-1][j] = 0
                        board[i][j] = buf
                        i += 1
                    else:
                        i -= 1

            elements = self.get_crashing_elements(board)

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
