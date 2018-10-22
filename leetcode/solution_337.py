#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.dfs(root))

    def dfs(self, root):
        if not root:
            return [0, 0]

        res = [0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        res[0] = root.val + left[1] + right[1]
        res[1] = max(left[0], left[1]) + max(right[0], right[1])

        return res

class TestSolution(unittest.TestCase):

    def test_rob(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(3)
        root.right.right = TreeNode(1)

        root2 = TreeNode(3)
        root2.left = TreeNode(4)
        root2.right = TreeNode(5)
        root2.left.left = TreeNode(1)
        root2.left.right = TreeNode(3)
        root2.right.right = TreeNode(1)

        solution = Solution()

        self.assertEqual(solution.rob(root), 7)
        self.assertEqual(solution.rob(root2), 9)

if __name__ == '__main__':
    unittest.main()
