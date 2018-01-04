#!/usr/bin/env python

import unittest

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for i, _ in enumerate(picture):
            for j, element in enumerate(picture[i]):
                if element == 'B':
                    if (all([picture[i][x] == 'W' for x in range(len(picture[i])) if x != j]) and
                            all([picture[x][j] == 'W' for x in range(len(picture)) if x != i])):
                        cnt += 1
        return cnt

class TestSolution(unittest.TestCase):

    def test_findLonelyPixel(self):
        picture = [['W', 'W', 'B'],
                   ['W', 'B', 'W'],
                   ['B', 'W', 'W']]
        picture2 = [['B', 'W', 'B'],
                    ['W', 'B', 'W'],
                    ['B', 'W', 'W']]
        solution = Solution()
        self.assertEqual(solution.findLonelyPixel(picture), 3)
        self.assertEqual(solution.findLonelyPixel(picture2), 1)

if __name__ == '__main__':
    unittest.main()
