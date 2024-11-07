#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def rec(root):
            if not root:
                return ''

            return (str(root.val) +
                    ('(' if root.left or root.right else '') +
                    str(rec(root.left)) +
                    (')' if root.left or root.right else '') +
                    ('(' if root.right else '') +
                    str(rec(root.right)) + (')' if root.right else ''))

        return rec(t)

class TestSolution(unittest.TestCase):

    def test_tree2str(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)

        solution = Solution()

        self.assertEqual(solution.tree2str(root), '1(2(4))(3)')

if __name__ == '__main__':
    unittest.main()
