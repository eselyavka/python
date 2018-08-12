#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root, arr):
    if root:
        inorder(root.left, arr)
        arr.append(root.val)
        inorder(root.right, arr)

def preorder(root, arr):
    if root:
        arr.append(root.val)
        preorder(root.left, arr)
        preorder(root.right, arr)

def postorder(root, arr):
    if root:
        postorder(root.left, arr)
        postorder(root.right, arr)
        arr.append(root.val)

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def _rec(root):
            if not root:
                return

            if root.val >= val and root.left is None:
                root.left = TreeNode(val)
                return

            if root.val < val and root.right is None:
                root.right = TreeNode(val)
                return

            if root.val >= val:
                _rec(root.left)

            if root.val < val:
                _rec(root.right)

        _rec(root)

        return root

class TestSolution(unittest.TestCase):

    def test_insertIntoBST(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        solution = Solution()
        expected = [1, 2, 3, 4, 5, 7]
        result = []
        new_root = solution.insertIntoBST(root, 5)

        inorder(new_root, result)

        self.assertListEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
