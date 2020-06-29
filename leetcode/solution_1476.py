#!/usr/bin/env python

import unittest


class SubrectangleQueries(object):
    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rect = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                self.rect[row][col] = newValue

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        return self.rect[row][col]


class TestSolution(unittest.TestCase):
    def test_SubrectangleQueries(self):
        solution = SubrectangleQueries([[1, 2, 1],
                                        [4, 3, 4],
                                        [3, 2, 1],
                                        [1, 1, 1]])
        self.assertEqual(solution.getValue(0, 2), 1)
        solution.updateSubrectangle(0, 0, 3, 2, 5)
        self.assertEqual(solution.getValue(0, 2), 5)
        self.assertEqual(solution.getValue(3, 1), 5)


if __name__ == '__main__':
    unittest.main()
