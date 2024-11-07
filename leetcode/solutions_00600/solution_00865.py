#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def height(self, root):
        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        return max(left, right) + 1

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 0

        height = self.height(root)
        def rec(root, curr, height):
            if not root or curr == height:
                return root

            left = rec(root.left, curr + 1, height)
            right = rec(root.right, curr + 1, height)

            return root if (left and right) else left or right

        return rec(root, 1, height)

class TestSolution(unittest.TestCase):

    def _inorder(self, root, arr):
        if not root:
            return

        self._inorder(root.left, arr)
        arr.append(root.val)
        self._inorder(root.right, arr)

    def test_subtreeWithAllDeepest(self):
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)

        root2 = TreeNode(0)
        root2.left = TreeNode(1)
        root2.left.right = TreeNode(2)
        root2.right = TreeNode(3)

        solution = Solution()
        buf = list()
        self._inorder(solution.subtreeWithAllDeepest(root), buf)
        self.assertListEqual(buf, [7, 2, 4])

        buf = list()
        self._inorder(solution.subtreeWithAllDeepest(root2), buf)
        self.assertListEqual(buf, [2])

if __name__ == '__main__':
    unittest.main()
