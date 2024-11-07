#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1 = []
        res2 = []

        def _rec(root, arr):
            if not root:
                return

            if not root.left and not root.right:
                arr.append(root.val)

            _rec(root.left, arr)
            _rec(root.right, arr)

        _rec(root1, res1)
        _rec(root2, res2)

        return res1 == res2


class Solution2(object):
    def traverse(self, root):
        stack = [root]
        leaf_nodes = list()
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not (node.right or node.left):
                leaf_nodes.append(node.val)
        return leaf_nodes

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf_nodes1 = self.traverse(root1)
        leaf_nodes2 = self.traverse(root2)

        return leaf_nodes1 == leaf_nodes2 if len(leaf_nodes1) == len(leaf_nodes1) else False


class TestSolution(unittest.TestCase):

    def test_leafSimilar(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)

        root2 = TreeNode(5)
        root2.left = TreeNode(1)
        root2.right = TreeNode(4)
        root2.right.left = TreeNode(3)
        root2.right.right = TreeNode(6)

        solution = Solution()
        self.assertTrue(solution.leafSimilar(root, root2))

        solution2 = Solution2()
        self.assertTrue(solution2.leafSimilar(root, root2))


if __name__ == '__main__':
    unittest.main()
