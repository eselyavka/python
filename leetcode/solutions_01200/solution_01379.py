#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        def hasPath(root, path, x, direction):
            if not root:
                return False

            if direction is not None:
                path.append(direction)

            if id(root) == id(x):
                return True

            if hasPath(root.left, path, x, True) or hasPath(root.right, path, x, False):
                return True

            path.pop(-1)

            return False

        path = []
        hasPath(original, path, target, None)

        def traverse(root, path, k):
            if k >= len(path):
                return root

            if path[k]:
                return traverse(root.left, path, k+1)

            return traverse(root.right, path, k+1)

        return traverse(cloned, path, 0)


class TestSolution(unittest.TestCase):

    def test_getTargetCopy(self):
        solution = Solution()

        root = TreeNode(7)
        root.left = TreeNode(4)
        root.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(19)

        root2 = TreeNode(7)
        root2.left = TreeNode(4)
        root2.right = TreeNode(3)
        root2.right.left = TreeNode(6)
        root2.right.right = TreeNode(19)

        self.assertEqual(solution.getTargetCopy(root,
                                                root2,
                                                root.right).val, 3)


if __name__ == '__main__':
    unittest.main()
