#!/usr/bin/env python3

"""LeetCode solution 00419."""

import unittest

class Solution(object):
    def adjacent(self, board, i, j):
        if i >= len(board) or j >= len(board[i]):
            return

        if board[i][j] == '.':
            return

        board[i][j] = '.'

        self.adjacent(board, i+1, j)
        self.adjacent(board, i, j+1)

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        num = 0
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == 'X':
                    num += 1
                    self.adjacent(board, i, j)
        return num

class TestSolution(unittest.TestCase):

    def test_countBattleships(self):
        board = [['X', '.', '.', 'X'],
                 ['.', '.', '.', 'X'],
                 ['.', '.', '.', 'X']]
        solution = Solution()
        self.assertEqual(solution.countBattleships(board), 2)

if __name__ == '__main__':
    unittest.main()
