#!/usr/bin/env python3

"""LeetCode solution 00366."""

import unittest
from collections import defaultdict

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        mem = defaultdict(list)

        def dfs(node):
            if not node:
                return -1

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            height = 1 + max(left_height, right_height)

            mem[height].append(node.val)
            return height

        dfs(root)
        return list(mem.values())

class TestSolution(unittest.TestCase):

    def test_findLeaves(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        solution = Solution()

        self.assertListEqual(solution.findLeaves(root), [[4, 5, 3], [2], [1]])

if __name__ == '__main__':
    unittest.main()
