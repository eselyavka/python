#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.left and not root.right:
            return 1

        s = set()

        def rec(root, s):
            if not root:
                return 0

            if root.val in s:
                s.remove(root.val)
            else:
                s.add(root.val)

            res = 0
            if not root.left and not root.right:
                res = 1 if len(s) <= 1 else 0
            else:
                res = res + rec(root.left, s) + rec(root.right, s)

            if root.val in s:
                s.remove(root.val)
            else:
                s.add(root.val)
            return res

        return rec(root, s)


class TestSolution(unittest.TestCase):
    def test_pseudoPalindromicPaths(self):
        solution = Solution()
        root = TreeNode(2)
        root.left = TreeNode(3)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)
        root.right = TreeNode(1)
        root.right.right = TreeNode(1)

        self.assertEqual(solution.pseudoPalindromicPaths(root), 2)


if __name__ == '__main__':
    unittest.main()
