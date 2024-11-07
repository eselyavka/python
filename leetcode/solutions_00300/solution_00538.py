#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    arr = []

    def _preorder(root):
        if not root:
            return

        arr.append(root.val)
        _preorder(root.left)
        _preorder(root.right)

    _preorder(root)

    return arr

class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        def rec(root):
            if not root:
                return

            rec(root.right)

            self.total += root.val
            root.val = self.total

            rec(root.left)

        rec(root)

        return root

class TestSolution(unittest.TestCase):

    def test_convertBST(self):
        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(13)

        solution = Solution()
        solution.convertBST(root)

        self.assertListEqual(preorder(root), [18, 20, 13])

        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(13)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(14)

        solution.convertBST(root)

        self.assertListEqual(preorder(root), [58, 60, 47, 53, 34])

if __name__ == '__main__':
    unittest.main()
