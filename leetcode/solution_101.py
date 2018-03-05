#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def rec(root, root2):
    if root and root2:
        opl = root.left if root.left is None else root.left.val
        opr = root.right if root.right is None else root.right.val
        op2l = root2.left if root2.left is None else root2.left.val
        op2r = root2.right if root2.right is None else root2.right.val
        return (opl == op2r and
                opr == op2l and
                rec(root.left, root2.right) and
                rec(root.right, root2.left))
    return True

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return rec(root, root)

class TestSolution(unittest.TestCase):

    def test_isSymmetric(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)

        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(2)
        root2.left.left = None
        root2.left.right = TreeNode(3)
        root2.right.left = None
        root2.right.right = TreeNode(3)

        root3 = TreeNode(4)

        solution = Solution()

        self.assertTrue(solution.isSymmetric(root))
        self.assertFalse(solution.isSymmetric(root2))
        self.assertTrue(solution.isSymmetric(root3))
        self.assertTrue(solution.isSymmetric(None))

if __name__ == '__main__':
    unittest.main()
