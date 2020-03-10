#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        arr = [0, 0]

        def dfs(root, x):
            if not root:
                return 0

            left = dfs(root.left, x)
            right = dfs(root.right, x)

            if root.val == x:
                arr[0], arr[1] = left, right

            return 1 + left + right

        dfs(root, x)

        return n/2 < max(max(arr), n - sum(arr) - 1)


class TestSolution(unittest.TestCase):

    def test_btreeGameWinningMove(self):
        solution = Solution()

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertFalse(solution.btreeGameWinningMove(root, 3, 1))


if __name__ == '__main__':
    unittest.main()
