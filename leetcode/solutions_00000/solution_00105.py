#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


class TestSolution(unittest.TestCase):

    def test_buildTree(self):
        solution = Solution([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        q = [solution]
        res = []

        while q:
            node = q.pop(0)
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        self.assertEqual(res, [3, 9, 20, 15, 7])


if __name__ == '__main__':
    unittest.main()
