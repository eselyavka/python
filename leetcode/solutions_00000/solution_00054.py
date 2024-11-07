#!/usr/bin/env python

import unittest


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        def rec(matrix, res, init_x, init_y, row, col):
            if init_x > len(matrix) - 1 or init_y > len(matrix[0]) - 1:
                return

            x = init_x
            y = init_y

            if matrix[x][y] != float('-inf'):
                res.append(matrix[x][y])

            matrix[x][y] = float('-inf')

            # right
            while y < col:
                y += 1
                if matrix[x][y] != float('-inf'):
                    res.append(matrix[x][y])
                    matrix[x][y] = float('-inf')

            # down
            while x < row:
                x += 1
                if matrix[x][y] != float('-inf'):
                    res.append(matrix[x][y])
                    matrix[x][y] = float('-inf')

            # left
            while y > init_y:
                y -= 1
                if matrix[x][y] != float('-inf'):
                    res.append(matrix[x][y])
                    matrix[x][y] = float('-inf')

            # up
            while x > init_x:
                x -= 1
                if matrix[x][y] != float('-inf'):
                    res.append(matrix[x][y])
                    matrix[x][y] = float('-inf')

            rec(matrix, res, init_x + 1, init_y + 1, row - 1, col - 1)

        if not matrix:
            return []

        res = []

        rec(matrix, res, 0, 0, len(matrix) - 1, len(matrix[0]) - 1)

        return res


class Solution2(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])

        ans = []
        left, right = 0, n
        top, bottom = 0, m
        while left < right and top < bottom:
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_spiralOrder(self):
        solution = Solution()
        self.assertListEqual(solution.spiralOrder([[1, 2, 3],
                                                   [4, 5, 6],
                                                   [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
        solution2 = Solution2()
        self.assertListEqual(solution2.spiralOrder([[1, 2, 3],
                                                    [4, 5, 6],
                                                    [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])


if __name__ == '__main__':
    unittest.main()
