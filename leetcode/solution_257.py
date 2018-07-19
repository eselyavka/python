#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        path = []

        def rec(root):
            if not root:
                return

            path.append(str(root.val))

            if root.left is None and root.right is None:
                paths.append("->".join(path))

            rec(root.left)
            rec(root.right)

            path.pop()

        rec(root)

        return paths


class TestSolution(unittest.TestCase):

    def test_binaryTreePaths(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)

        root2 = TreeNode(1)
        root2.left = TreeNode(0)
        root2.right = TreeNode(48)
        root2.right.left = TreeNode(12)
        root2.right.right = TreeNode(49)

        solution = Solution()

        self.assertListEqual(solution.binaryTreePaths(root), ["1->2->5", "1->3"])
        self.assertListEqual(solution.binaryTreePaths(root2), ["1->0", "1->48->12", "1->48->49"])

if __name__ == '__main__':
    unittest.main()
