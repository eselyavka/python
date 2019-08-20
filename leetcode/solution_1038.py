#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    total = 0

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        self.bstToGst(root.right)

        self.total += root.val
        root.val = self.total

        self.bstToGst(root.left)

        return root


class TestSolution(unittest.TestCase):

    def test_bstToGst(self):
        solution = Solution()

        root = TreeNode(4)
        root.left = TreeNode(1)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(2)
        root.left.right.right = TreeNode(3)
        root.right = TreeNode(6)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        root.right.right.right = TreeNode(8)

        solution.bstToGst(root)

        actual = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            actual.append(root.val)
            inorder(root.right)

        inorder(root)

        self.assertListEqual(actual, [36, 36, 35, 33, 30, 26, 21, 15, 8])

if __name__ == '__main__':
    unittest.main()
