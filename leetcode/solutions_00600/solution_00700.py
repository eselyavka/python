#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(arr, root):
    if root:
        inorder(arr, root.left)
        arr.append(root.val)
        inorder(arr, root.right)

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)

        return root

class TestSolution(unittest.TestCase):

    def test_searchBST(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        solution = Solution()
        expected = []
        inorder(expected, solution.searchBST(root, 2))

        self.assertEqual(expected, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
