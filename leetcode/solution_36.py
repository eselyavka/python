#!/usr/bin/env python

import unittest
from collections import defaultdict

class Solution(object):
    def is_valid_num(self, num):
        try:
            num = int(num)
            return 1 <= num <= 9
        except ValueError:
            if num == '.':
                return True

        return False
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d_row = defaultdict(set)
        d_col = defaultdict(set)
        sub_i = 1
        setA = set()
        setB = set()
        setC = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                num_row = board[row][col]
                num_col = board[col][row]
                if not self.is_valid_num(num_row) or num_row in d_row[row]:
                    return False
                else:
                    if num_row != '.':
                        d_row[row].add(num_row)

                if not self.is_valid_num(num_col) or num_col in d_col[row]:
                    return False
                else:
                    if num_col != '.':
                        d_col[row].add(num_col)

                if col // 3 == 0:
                    if num_row in setA:
                        return False
                    else:
                        if num_row != '.':
                            setA.add(num_row)

                if col // 3 == 1:
                    if num_row in setB:
                        return False
                    else:
                        if num_row != '.':
                            setB.add(num_row)

                if col // 3 == 2:
                    if num_row in setC:
                        return False
                    else:
                        if num_row != '.':
                            setC.add(num_row)

            if sub_i % 3 == 0:
                setA.clear()
                setB.clear()
                setC.clear()
            sub_i += 1

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
