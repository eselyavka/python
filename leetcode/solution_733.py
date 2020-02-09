#!/usr/bin/env python

import unittest


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        seen = [[False for _ in range(len(image[i]))] for i in range(len(image))]

        def fill(matrix, sr, sc, oldColor, newColor):
            if sr >= len(matrix) or sr < 0 or sc >= len(matrix[0]) or sc < 0:
                return

            if matrix[sr][sc] != oldColor or seen[sr][sc]:
                return

            seen[sr][sc] = True
            matrix[sr][sc] = newColor

            # up
            fill(matrix, sr+1, sc, oldColor, newColor)
            # down
            fill(matrix, sr-1, sc, oldColor, newColor)
            # right
            fill(matrix, sr, sc+1, oldColor, newColor)
            # left
            fill(matrix, sr, sc-1, oldColor, newColor)

        fill(image, sr, sc, image[sr][sc], newColor)

        return image


class TestSolution(unittest.TestCase):

    def test_floodFill(self):
        solution = Solution()

        self.assertEqual(solution.floodFill(
            [[1, 1, 1],
             [1, 1, 0],
             [1, 0, 1]], 1, 1, 2),
                         [[2, 2, 2],
                          [2, 2, 0],
                          [2, 0, 1]])

        self.assertEqual(solution.floodFill(
            [[0, 0, 0], [0, 0, 0]], 0, 0, 2),
                         [[2, 2, 2], [2, 2, 2]])


if __name__ == '__main__':
    unittest.main()
