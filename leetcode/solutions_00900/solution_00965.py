#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s = set()

        def rec(root):
            if not root:
                return

            s.add(root.val)

            rec(root.left)
            rec(root.right)

        rec(root)

        return len(s) == 1


class TestSolution(unittest.TestCase):

    def test_isUnivalTree(self):
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.right.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)

        root2 = TreeNode(2)
        root2.left = TreeNode(2)
        root2.right = TreeNode(2)
        root2.left.left = TreeNode(5)
        root2.left.right = TreeNode(2)

        solution = Solution()

        self.assertTrue(solution.isUnivalTree(root))
        self.assertFalse(solution.isUnivalTree(root2))

if __name__ == '__main__':
    unittest.main()
