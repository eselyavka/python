#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.flag = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def rec(root):
            if not root:
                return 0

            left = rec(root.left)
            right = rec(root.right)

            if abs(left - right) > 1:
                self.flag = False

            if left > right:
                return left + 1

            return right + 1


        rec(root)

        return self.flag

class TestSolution(unittest.TestCase):

    def test_isBalanced(self):
        solution = Solution()

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertTrue(solution.isBalanced(root))

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)

        self.assertFalse(solution.isBalanced(root))

if __name__ == '__main__':
    unittest.main()
