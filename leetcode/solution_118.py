#!/usr/bin/env python

import unittest


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        res = [[1]] if numRows else []

        for i in range(1, numRows):
            res.append(self.getRow(i))

        return res

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        arr = [1]
        for i in range(rowIndex):
            arr.append(arr[i]*(rowIndex-i)/(i+1))
        return arr


class Solution2(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        matrix = [[1]*(i+1) for i in range(numRows)]

        for i in range(numRows):
            for j in range(1, i):
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]

        return matrix


class TestSolution(unittest.TestCase):
    def test_generate(self):
        solution = Solution()
        self.assertEqual(solution.generate(5), [[1],
                                                [1, 1],
                                                [1, 2, 1], [1, 3, 3, 1],
                                                [1, 4, 6, 4, 1]])
        solution2 = Solution2()
        self.assertEqual(solution2.generate(5), [[1],
                                                 [1, 1],
                                                 [1, 2, 1],
                                                 [2, 3, 3, 1],
                                                 [1, 4, 6, 4, 1]])


if __name__ == '__main__':
    unittest.main()
