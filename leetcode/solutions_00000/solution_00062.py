#!/usr/bin/env python

import unittest

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    paths[i][j] = 1
                else:
                    paths[i][j] = paths[i][j-1] + paths[i-1][j]

        return paths[n-1][m-1]

class TestSolution(unittest.TestCase):

    def test_uniquePaths(self):
        solution = Solution()

        self.assertEqual(solution.uniquePaths(3, 2), 3)

if __name__ == '__main__':
    unittest.main()
