#!/usr/bin/env python

import unittest
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = defaultdict(int)

        def rec(root, level):
            if not root:
                return
            d[level] += root.val
            rec(root.left, level + 1)
            rec(root.right, level + 1)

        rec(root, 1)

        arr = d.items()
        arr.sort(key=lambda x: x[1])

        return arr[-1][0]


class TestSolution(unittest.TestCase):

    def test_maxLevelSum(self):
        solution = Solution()

        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(-8)

        self.assertEqual(solution.maxLevelSum(root), 2)


if __name__ == '__main__':
    unittest.main()
