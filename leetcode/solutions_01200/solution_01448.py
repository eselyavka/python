#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def rec(root, max_):
            if not root:
                return 0

            return (1 if root.val >= max_ else 0) + rec(root.left,
                                                        max(max_, root.val)) + rec(root.right,
                                                                                   max(max_, root.val))

        return rec(root, root.val)


class TestSolution(unittest.TestCase):

    def test_goodNodes(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.left = TreeNode(3)
        root.right = TreeNode(4)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)

        solution = Solution()

        self.assertEqual(solution.goodNodes(root), 4)


if __name__ == '__main__':
    unittest.main()
