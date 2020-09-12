#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = 0

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def rec(root, L, R):
            if root:
                if root.val >= L and root.val <= R:
                    self.res += root.val
                if root.val > L:
                    rec(root.left, L, R)
                if root.val < R:
                    rec(root.right, L, R)

        rec(root, L, R)

        return self.res


class TestSolution(unittest.TestCase):

    def test_rangeSumBST(self):
        solution = Solution()

        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right = TreeNode(15)
        root.right.right = TreeNode(18)

        self.assertEqual(solution.rangeSumBST(root, 7, 15), 32)

        solution = Solution()

        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(1)
        root.left.right = TreeNode(7)
        root.left.right.left = TreeNode(6)
        root.right = TreeNode(15)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(18)

        self.assertEqual(solution.rangeSumBST(root, 6, 10), 23)


if __name__ == '__main__':
    unittest.main()
