#!/usr/bin/env python3

"""LeetCode solution 00129."""

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rec(root, total):
            if not root:
                return 0

            total = total * 10 + root.val

            if root.left is None and root.right is None:
                return total

            return rec(root.left, total) + rec(root.right, total)

        return rec(root, 0)


class TestSolution(unittest.TestCase):

    def test_sumNumbers(self):
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)

        solution = Solution()

        self.assertEqual(solution.sumNumbers(root), 1026)


if __name__ == '__main__':
    unittest.main()
