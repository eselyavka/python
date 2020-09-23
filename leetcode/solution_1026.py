#!/usr/bin/env python
import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rec(root, max_, min_):
            if not root:
                return max_ - min_

            return max(rec(root.left, max(max_, root.val), min(min_, root.val)),
                       rec(root.right, max(max_, root.val), min(min_, root.val)))

        return rec(root, -1, 100001)


class TestSolution(unittest.TestCase):
    def test_maxAncestorDiff(self):
        solution = Solution()

        root = TreeNode(8)
        root.left = TreeNode(3)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(7)
        root.right = TreeNode(10)
        root.right.right = TreeNode(14)
        root.right.right.left = TreeNode(13)

        self.assertEqual(solution.maxAncestorDiff(root), 7)


if __name__ == '__main__':
    unittest.main()
