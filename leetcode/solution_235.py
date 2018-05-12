#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def _tree_traversals(self, root, arr, x):
        if root is None:
            return False

        arr.append(root)

        if root.val == x.val:
            return True

        if ((root.left is not None and self._tree_traversals(root.left, arr, x)) or
                (root.right is not None and self._tree_traversals(root.right, arr, x))):
            return True

        arr.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_arr = []
        q_arr = []
        self._tree_traversals(root, p_arr, p)
        self._tree_traversals(root, q_arr, q)

        i = 0
        while i < len(p_arr) and i < len(q_arr):
            if p_arr[i] != q_arr[i]:
                break
            i += 1

        return p_arr[i-1]

class TestSolution(unittest.TestCase):

    def test_lowestCommonAncestor(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        solution = Solution()

        self.assertEqual(solution.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val, 6)
        self.assertEqual(solution.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val, 2)

if __name__ == '__main__':
    unittest.main()
