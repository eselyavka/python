#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def heigh(root):
            if not root:
                return 0

            return 1 + max(heigh(root.left), heigh(root.right))

        left = heigh(root.left)
        right = heigh(root.right)

        ans = abs(left - right)

        return ans < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)


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
