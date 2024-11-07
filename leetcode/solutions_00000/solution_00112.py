#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def rec(root, _sum):
            if not root:
                return False

            sub_sum = _sum - root.val

            if root.left is None and root.right is None and sub_sum == 0:
                return True

            return rec(root.left, sub_sum) or rec(root.right, sub_sum)

        return rec(root, sum)

class TestSolution(unittest.TestCase):

    def test_hasPathSum(self):
        solution = Solution()

        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)

        self.assertTrue(solution.hasPathSum(root, 22))

if __name__ == '__main__':
    unittest.main()
