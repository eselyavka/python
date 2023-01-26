#!/usr/bin/env python

import unittest


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = col = len(board)

        def is_unique_arr(arr):
            return len(arr) == len(set(arr))

        square1, square2, square3 = [], [], []
        for i in range(row):
            r = []
            c = []
            for j in range(col):
                if board[i][j] != ".":
                    r.append(board[i][j])
                if board[j][i] != ".":
                    c.append(board[j][i])

                if j <= 2 and board[i][j] != ".":
                    square1.append(board[i][j])
                elif 2 < j <= 5 and board[i][j] != ".":
                    square2.append(board[i][j])
                elif 5 < j <= 8 and board[i][j] != ".":
                    square3.append(board[i][j])

            if i == 2:
                if not is_unique_arr(square1) or not is_unique_arr(square2) or not is_unique_arr(square3):
                    return False
                square1, square2, square3 = [], [], []
            if i == 5:
                if not is_unique_arr(square1) or not is_unique_arr(square2) or not is_unique_arr(square3):
                    return False
                square1, square2, square3 = [], [], []
            if i == 8:
                if not is_unique_arr(square1) or not is_unique_arr(square2) or not is_unique_arr(square3):
                    return False
                square1, square2, square3 = [], [], []

            if not is_unique_arr(r):
                return False
            if not is_unique_arr(c):
                return False

        return True


class TestSolution(unittest.TestCase):

    def test_isValidSudoku(self):
        solution = Solution()
        sudoku1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                   [".", "9", "8", ".", ".", ".", ".", "6", "."],
                   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                   [".", "6", ".", ".", ".", ".", "2", "8", "."],
                   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                   [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        self.assertTrue(solution.isValidSudoku(sudoku1))
        sudoku1[0][0] = "8"
        self.assertFalse(solution.isValidSudoku(sudoku1))
        sudoku1[0][0] = "5"
        sudoku1[8][1] = "6"
        self.assertFalse(solution.isValidSudoku(sudoku1))
        sudoku1[4][6] = "3"
        self.assertFalse(solution.isValidSudoku(sudoku1))


if __name__ == '__main__':
    unittest.main()
