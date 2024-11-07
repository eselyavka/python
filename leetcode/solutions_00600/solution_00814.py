#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def rec(root):
            if not root:
                return None

            root.left = rec(root.left)
            root.right = rec(root.right)

            if root.val == 0 and root.left is None and root.right is None:
                return None

            return root

        root = rec(root)

        return root

class TestSolution(unittest.TestCase):

    def test_pruneTree(self):
        root = TreeNode(1)
        root.right = TreeNode(0)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)

        actual = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            actual.append(root.val)
            inorder(root.right)

        inorder(Solution().pruneTree(root))

        self.assertListEqual(actual, [1, 0, 1])

if __name__ == '__main__':
    unittest.main()
