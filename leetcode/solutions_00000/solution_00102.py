#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def height(self, root):
        if root is None:
            return 0

        left_height = 1 + self.height(root.left)
        right_height = 1 + self.height(root.right)

        return left_height if left_height > right_height else right_height

    def level_traversals(self, root, level):
        if root is None:
            return []

        if level == 1:
            return [root.val]

        r = self.level_traversals(root.left, level - 1)
        l = self.level_traversals(root.right, level - 1)

        res = (r if r else []) + (l if l else [])
        return res

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(1, self.height(root)+1):
            arr.append(self.level_traversals(root, i))
        return arr


class TestSolution(unittest.TestCase):

    def test_levelOrder(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        solution = Solution()

        self.assertEqual(solution.levelOrder(root), [[3], [9, 20], [15, 7]])

if __name__ == '__main__':
    unittest.main()
