#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def height(self, root):
        if root:
            return 1 + self.height(root.left)
        return -1

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        height = self.height(root)
        if height < 0:
            return 0

        rheight = self.height(root.right)

        if rheight == height - 1:
            return (1 << height) + self.countNodes(root.right)

        return (1 << height - 1) + self.countNodes(root.left)

class TestSolution(unittest.TestCase):

    def test_findTarget(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.left.left.right = TreeNode(10)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(14)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        root.right.left.left = TreeNode(2)

        solution = Solution()
        self.assertEqual(solution.countNodes(root), 12)

if __name__ == '__main__':
    unittest.main()
