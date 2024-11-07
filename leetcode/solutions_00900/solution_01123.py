#!/usr/bin/env python
import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.depth = 0

    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def depth(root, d):
            if not root:
                self.depth = max(self.depth, d)
                return

            depth(root.left, d+1)
            depth(root.right, d+1)

        depth(root, 0)

        def rec(node, curr):
            if not node or curr == self.depth:
                return node

            left = rec(node.left, curr+1)
            right = rec(node.right, curr+1)

            return node if (left and right) else (left or right)

        return rec(root, 1)


class TestSolution(unittest.TestCase):
    def test_lcaDeepestLeaves(self):
        solution = Solution()

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        actual = solution.lcaDeepestLeaves(root)

        self.assertEqual([actual.val,
                          actual.left.val,
                          actual.right.val], [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
