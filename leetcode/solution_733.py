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
        old_color = image[sr][sc]

        def fill(sr, sc):
            if sr < 0 or sc < 0:
                return

            if sr >= len(image) or sc >= len(image[sr]):
                return

            if image[sr][sc] != old_color or seen[sr][sc]:
                return

            image[sr][sc] = newColor
            seen[sr][sc] = True

            fill(sr + 1, sc)
            fill(sr - 1, sc)
            fill(sr, sc + 1)
            fill(sr, sc - 1)

        fill(sr, sc)

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
