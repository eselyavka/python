#!/usr/bin/env python

import unittest
import copy
import math

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        def smooth(i, j):
            if i >= len(M) or i < 0:
                return (0, 0)
            if j >= len(M[0]) or j < 0:
                return (0, 0)

            return (1, M[i][j])

        res = copy.deepcopy(M)

        for i in range(len(M)):
            for j in range(len(M[0])):
                total, total_values = 0, 0
                total += smooth(i, j)[0]
                total_values += smooth(i, j)[1]

                total += smooth(i-1, j)[0]
                total_values += smooth(i-1, j)[1]
                total += smooth(i+1, j)[0]
                total_values += smooth(i+1, j)[1]

                total += smooth(i, j-1)[0]
                total_values += smooth(i, j-1)[1]
                total += smooth(i, j+1)[0]
                total_values += smooth(i, j+1)[1]

                total += smooth(i-1, j-1)[0]
                total_values += smooth(i-1, j-1)[1]
                total += smooth(i-1, j+1)[0]
                total_values += smooth(i-1, j+1)[1]

                total += smooth(i+1, j-1)[0]
                total_values += smooth(i+1, j-1)[1]
                total += smooth(i+1, j+1)[0]
                total_values += smooth(i+1, j+1)[1]

                res[i][j] = int(math.floor(total_values/total))

        return res

class TestSolution(unittest.TestCase):

    def test_imageSmoother(self):
        solution = Solution()

        self.assertEqual(solution.imageSmoother([[2, 3, 4],
                                                 [5, 6, 7],
                                                 [8, 9, 10],
                                                 [11, 12, 13],
                                                 [14, 15, 16]]), [[4, 4, 5],
                                                                  [5, 6, 6],
                                                                  [8, 9, 9],
                                                                  [11, 12, 12],
                                                                  [13, 13, 14]])

if __name__ == '__main__':
    unittest.main()
