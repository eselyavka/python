#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def _rec(self, root, target, d):
        if root:
            diff = abs(target - root.val)
            d[diff] = root.val
            self._rec(root.left, target, d)
            self._rec(root.right, target, d)

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        d = dict()

        self._rec(root, target, d)

        return d[min(d.keys())]

class TestSolution(unittest.TestCase):

    def test_closestValue(self):
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
        root.right.left.left = TreeNode(-2)

        solution = Solution()
        self.assertEqual(solution.closestValue(root, 15), 14)
        self.assertEqual(solution.closestValue(root, 0), 1)
        self.assertEqual(solution.closestValue(root, -10), -2)
        self.assertEqual(solution.closestValue(root, 8), 7)

if __name__ == '__main__':
    unittest.main()
