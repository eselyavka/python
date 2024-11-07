#!/usr/bin/env python

import unittest

class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid:
            return None

        def is_leaf(matrix):
            if len(matrix) == 1:
                return True

            s = set()
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    s.add(matrix[i][j])
                    if len(s) > 1:
                        return False
            return True

        def rec(matrix):
            n = len(matrix)

            leaf = is_leaf(matrix)

            if leaf:
                return Node(leaf, leaf, None, None, None, None)

            return Node('*',
                        False,
                        rec([row[:n//2] for row in matrix[:n//2]]),
                        rec([row[n//2:] for row in matrix[:n//2]]),
                        rec([row[:n//2] for row in matrix[n//2:]]),
                        rec([row[n//2:] for row in matrix[n//2:]]))

        return rec(grid)


class TestSolution(unittest.TestCase):

    def test_construct(self):
        solution = Solution()

        self.assertTrue(isinstance(solution.construct([[1, 1, 1, 1, 0, 0, 0, 0],
                                                       [1, 1, 1, 1, 0, 0, 0, 0],
                                                       [1, 1, 1, 1, 1, 1, 1, 1],
                                                       [1, 1, 1, 1, 1, 1, 1, 1],
                                                       [1, 1, 1, 1, 0, 0, 0, 0],
                                                       [1, 1, 1, 1, 0, 0, 0, 0],
                                                       [1, 1, 1, 1, 0, 0, 0, 0],
                                                       [1, 1, 1, 1, 0, 0, 0, 0]]), Node))

if __name__ == '__main__':
    unittest.main()
