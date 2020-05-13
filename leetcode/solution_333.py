#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def isBSTUtil(self, node, min_, max_):
        if node is None:
            return True
        if node.val < min_ or node.val > max_:
            return False
        return self.isBSTUtil(node.left, min_, node.val - 1) and self.isBSTUtil(node.right, node.val + 1, max_)

    def isBST(self, node):
        return self.isBSTUtil(node, float('-inf'), float('+inf'))

    def size(self, root):
        if not root:
            return 0
        return 1 + self.size(root.left) + self.size(root.right)

    def largestBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return 0

        if self.isBST(root):
            return self.size(root)
        return max(self.largestBST(root.left), self.largestBST(root.right))


class TestSolution(unittest.TestCase):

    def test_isBST(self):
        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(4)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        solution = Solution()

        self.assertEqual(solution.largestBST(root), 3)


if __name__ == '__main__':
    unittest.main()
