#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        def rec(root, d):
            if root:
                if not root.left and not root.right:
                    return d
                return min(rec(root.left, d+1) if root.left else float('+inf'),
                           rec(root.right, d+1) if root.right else float('+inf'))
            return d

        return rec(root, 1)

class TestSolution(unittest.TestCase):

    def test_minDepth(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)

        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.right = TreeNode(3)

        root3 = TreeNode(10)

        root4 = TreeNode(0)
        root4.left = TreeNode(-1)

        root5 = TreeNode(1)
        root5.left = TreeNode(2)
        root5.left.left = TreeNode(3)
        root5.left.left.left = TreeNode(4)
        root5.left.left.left.left = TreeNode(5)

        solution = Solution()

        self.assertEqual(solution.minDepth(root), 2)
        self.assertEqual(solution.minDepth(root2), 2)
        self.assertEqual(solution.minDepth(root3), 1)
        self.assertEqual(solution.minDepth(root4), 2)
        self.assertEqual(solution.minDepth(root5), 5)

if __name__ == '__main__':
    unittest.main()
