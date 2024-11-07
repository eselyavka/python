import unittest


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        row = set()
        column = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)

        for i in range(n):
            for j in range(m):
                if i in row or j in column:
                    matrix[i][j] = 0


class TestSolution(unittest.TestCase):
    def test_setZeroes(self):
        solution = Solution()
        actual = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        solution.setZeroes(actual)
        self.assertListEqual(actual, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])


if __name__ == '__main__':
    unittest.main()
