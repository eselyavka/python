#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        def height(root):
            if root is None:
                return 0

            left = height(root.left)
            right = height(root.right)

            return 1 + max(left, right)

        left = height(root.left)
        right = height(root.right)

        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(left + right, max(left_diameter, right_diameter))


class TestSolution(unittest.TestCase):

    def test_diameterOfBinaryTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        root2.right.right = TreeNode(8)
        root2.right.right.right = TreeNode(9)
        root2.right.right.right.left = TreeNode(10)
        root2.right.right.right.right = TreeNode(11)
        root2.right.right.right.left.right = TreeNode(12)
        root2.left.left = TreeNode(4)
        root2.left.right = TreeNode(5)
        root2.left.right.left = TreeNode(6)
        root2.left.right.right = TreeNode(7)

        solution = Solution()

        self.assertEqual(solution.diameterOfBinaryTree(root), 3)
        self.assertEqual(solution.diameterOfBinaryTree(root2), 8)


if __name__ == '__main__':
    unittest.main()
