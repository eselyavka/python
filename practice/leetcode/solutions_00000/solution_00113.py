#!/usr/bin/env python3

"""LeetCode solution 00113."""

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, target_sum):
        """
        :type root: TreeNode
        :type target_sum: int
        :rtype: int
        """
        if not root:
            return []

        res = []

        def rec(node, target, paths):
            if not node:
                return

            if node.left is None and node.right is None and node.val == target:
                paths.append(node.val)
                res.append(paths)

            if node.left:
                rec(node.left, target - node.val, paths + [node.val])
            if node.right:
                rec(node.right, target - node.val, paths + [node.val])

        rec(root, target_sum, [])

        return res

class TestSolution(unittest.TestCase):

    def test_pathSum(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(-3)
        root.right.right = TreeNode(11)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)
        root.left.right.right = TreeNode(1)
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)

        self.assertListEqual(Solution().pathSum(root, 8), [])

        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)

        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.right = None

        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)

        self.assertListEqual(Solution().pathSum(root, 22), [[5, 4, 11, 2], [5, 8, 4, 5]])

if __name__ == '__main__':
    unittest.main()
