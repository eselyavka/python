#!/usr/bin/env python

import unittest


class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        return list(set(range(n)) - set([v[1] for v in edges]))


class TestSolution(unittest.TestCase):
    def test_findSmallestSetOfVertices(self):
        solution = Solution()
        self.assertListEqual(solution.findSmallestSetOfVertices(6, [[0, 1],
                                                                    [0, 2],
                                                                    [2, 5],
                                                                    [3, 4],
                                                                    [4, 2]]), [0, 3])


if __name__ == '__main__':
    unittest.main()
