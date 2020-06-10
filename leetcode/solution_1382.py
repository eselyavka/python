#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)

        def buildtree(arr, s, e):
            if s > e:
                return None

            mid = (s + e) // 2

            root = TreeNode(arr[mid])

            if s == e:
                return root

            root.left = buildtree(arr, s, mid - 1)
            root.right = buildtree(arr, mid + 1, e)

            return root

        res = buildtree(arr, 0, len(arr) - 1)

        return res


class TestSolution(unittest.TestCase):

    def test_balanceBST(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)

        solution = Solution()
        balanced_tree = solution.balanceBST(root)

        self.assertEqual(balanced_tree.val, 2)
        self.assertEqual(balanced_tree.left.val, 1)
        self.assertEqual(balanced_tree.right.val, 3)
        self.assertEqual(balanced_tree.right.right.val, 4)


if __name__ == '__main__':
    unittest.main()
