#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self._max = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rec(node):
            if not node:
                return 0

            left = rec(node.left)
            right = rec(node.right)

            leftmax, rightmax = 0, 0
            if node.left and node.left.val == node.val:
                leftmax = left + 1
            if node.right and node.right.val == node.val:
                rightmax = right + 1

            self._max = max(self._max, leftmax + rightmax)

            return max(leftmax, rightmax)

        rec(root)

        return self._max

class TestSolution(unittest.TestCase):

    def test_longestUnivaluePath(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.right.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)

        self.assertEqual(Solution().longestUnivaluePath(root), 2)

        root = TreeNode(1)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.right.right = TreeNode(5)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(4)

        self.assertEqual(Solution().longestUnivaluePath(root), 2)

if __name__ == '__main__':
    unittest.main()
