#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.m = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rec(root):
            if not root:
                return 0

            left = rec(root.left)
            right = rec(root.right)

            node = max(max(left, right) + root.val, root.val)
            all_ = max(node, root.val + left + right)

            self.m = max(self.m, all_)

            return node

        rec(root)

        return self.m


class TestSolution(unittest.TestCase):

    def test_maxPathSum(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        solution = Solution()

        self.assertEqual(solution.maxPathSum(root), 6)


if __name__ == '__main__':
    unittest.main()
