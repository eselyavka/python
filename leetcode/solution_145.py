#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            n = stack.pop()

            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)

            res = [n.val] + res

        return res

class TestSolution(unittest.TestCase):

    def test_postorderTraversal(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)

        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.right = TreeNode(3)

        root3 = TreeNode(10)

        root4 = TreeNode(0)
        root4.left = TreeNode(-1)

        root5 = TreeNode(0)
        root5.right = TreeNode(100)

        root6 = TreeNode(0)
        root6.right = TreeNode(-100)

        root7 = TreeNode(10)
        root7.left = TreeNode(5)
        root7.right = TreeNode(15)
        root7.right.left = TreeNode(6)
        root7.right.right = TreeNode(20)

        solution = Solution()

        self.assertEqual(solution.postorderTraversal(root), [1, 3, 6, 4, 5])
        self.assertEqual(solution.postorderTraversal(None), [])
        self.assertEqual(solution.postorderTraversal(root2), [1, 3, 2])
        self.assertEqual(solution.postorderTraversal(root3), [10])
        self.assertEqual(solution.postorderTraversal(root4), [-1, 0])
        self.assertEqual(solution.postorderTraversal(root5), [100, 0])
        self.assertEqual(solution.postorderTraversal(root6), [-100, 0])
        self.assertEqual(solution.postorderTraversal(root7), [5, 6, 20, 15, 10])

if __name__ == '__main__':
    unittest.main()
