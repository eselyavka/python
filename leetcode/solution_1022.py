#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        path = []

        def rec(root, path):
            if not root:
                return

            path.append(str(root.val))

            if not root.left and not root.right:
                res.append(int(''.join(path), 2))

            rec(root.left, path)
            rec(root.right, path)

            path.pop()

        rec(root, path)

        return sum(res)


class TestSolution(unittest.TestCase):

    def test_sumRootToLeaf(self):
        solution = Solution()

        root = TreeNode(1)
        root.left = TreeNode(0)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(1)
        root.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)

        self.assertEqual(solution.sumRootToLeaf(root), 22)


if __name__ == '__main__':
    unittest.main()
