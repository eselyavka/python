#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = None

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        s = [root]

        while s:
            buf = s.pop()
            res.append(buf.val)
            while buf.children:
                child = buf.children.pop()
                s.append(child)

        return res

class TestSolution(unittest.TestCase):

    def test_preorder(self):
        root = TreeNode(1)
        child = TreeNode(3)
        root.children = [child, TreeNode(2), TreeNode(4)]
        child.children = [TreeNode(5), TreeNode(6)]

        solution = Solution()

        self.assertEqual(solution.preorder(root), [1, 3, 5, 6, 2, 4])

if __name__ == '__main__':
    unittest.main()
