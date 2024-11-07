#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def minimumKeyInLeft(self, curr):
        while curr.right:
            curr = curr.right

        return curr

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            else:
                tmp = self.minimumKeyInLeft(root.left)
                root.val = tmp.val
                root.left = self.deleteNode(root.left, tmp.val)

        return root


class TestSolution(unittest.TestCase):

    @staticmethod
    def inorder(root, arr):
        if not root:
            return

        TestSolution.inorder(root.left, arr)
        arr.append(root.val)
        TestSolution.inorder(root.right, arr)

    def init_tree(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right = TreeNode(6)
        root.right.right = TreeNode(7)

        return root

    def test_deleteNode(self):
        solution = Solution()

        root = self.init_tree()
        res = solution.deleteNode(root, 7)
        arr = []
        TestSolution.inorder(res, arr)
        self.assertListEqual(arr, [2, 3, 4, 5, 6])

        root = self.init_tree()
        res = solution.deleteNode(root, 6)
        arr = []
        TestSolution.inorder(res, arr)
        self.assertListEqual(arr, [2, 3, 4, 5, 7])

        root = self.init_tree()
        res = solution.deleteNode(root, 3)
        arr = []
        TestSolution.inorder(res, arr)
        self.assertListEqual(arr, [2, 4, 5, 6, 7])

        root = TreeNode(0)
        res = solution.deleteNode(root, 0)
        arr = []
        TestSolution.inorder(root, arr)
        self.assertIsNone(res)


if __name__ == '__main__':
    unittest.main()
