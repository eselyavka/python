#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if s is None and t is None:
            return True

        if s is None or t is None:
            return False

        def rec(s, t):
            if not s and not t:
                return True

            if not s or not t:
                return False

            return s.val == t.val and rec(s.left, t.left) and rec(s.right, t.right)

        if rec(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

class TestSolution(unittest.TestCase):

    def test_isSubtree(self):
        solution = Solution()

        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)

        root2 = TreeNode(4)
        root2.left = TreeNode(1)
        root2.right = TreeNode(2)

        self.assertTrue(solution.isSubtree(root, root2))

        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(0)

        self.assertFalse(solution.isSubtree(root, root2))

if __name__ == '__main__':
    unittest.main()
