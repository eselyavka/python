#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        def height(root):
            if not root:
                return 0
            left = 1 + height(root.left)
            right = 1 + height(root.right)

            return left if right < left else left

        h = height(root)

        def rec(root, target):
            if not root:
                return None
            root.left = rec(root.left, target)
            root.right = rec(root.right, target)

            if root.val == target and not root.left and not root.right:
                return None

            return root

        for _ in range(h):
            res = rec(root, target)

        return res


class TestSolution(unittest.TestCase):

    def test_removeLeafNodes(self):
        solution = Solution()

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(4)

        solution.removeLeafNodes(root, 2)

        actual = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            actual.append(root.val)
            inorder(root.right)

        inorder(root)

        self.assertListEqual(actual, [1, 3, 4])


if __name__ == '__main__':
    unittest.main()
