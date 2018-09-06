#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def rec(root, is_left=False):
            if not root:
                return

            if is_left and root.right is None and root.left is None:
                res.append(root.val)

            rec(root.left, is_left=True)
            rec(root.right)

        rec(root)

        return sum(res)

class TestSolution(unittest.TestCase):

    def test_sumOfLeftLeaves(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        solution = Solution()

        self.assertEqual(solution.sumOfLeftLeaves(root), 24)

if __name__ == '__main__':
    unittest.main()
