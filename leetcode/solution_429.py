#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        s = [root]

        while s:
            level = []
            while s:
                node = s.pop(0)
                level.append(node)

            res.append([node.val for node in level])
            [s.extend(node.children) for node in level if node.children]

        return res

class TestSolution(unittest.TestCase):

    def test_levelOrder(self):
        root = TreeNode(1)
        child = TreeNode(3)
        root.children = [child, TreeNode(2), TreeNode(4)]
        child.children = [TreeNode(5), TreeNode(6)]

        solution = Solution()

        self.assertEqual(solution.levelOrder(root),
                         [[1], [3, 2, 4], [5, 6]])

if __name__ == '__main__':
    unittest.main()
