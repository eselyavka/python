#!/usr/bin/env python

import unittest
import string


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = ''

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        mapping = dict(zip(range(26), string.ascii_lowercase))
        self.res = ''

        def dfs(root, s):
            if not root:
                return

            if not root.left and not root.right:
                leaf_str = mapping.get(root.val) + s
                self.res = min(leaf_str, self.res or 'z' * len(leaf_str))

            dfs(root.left, mapping.get(root.val)+s)
            dfs(root.right, mapping.get(root.val)+s)

        dfs(root, '')

        return self.res


class TestSolution(unittest.TestCase):
    def test_smallestFromLeaf(self):
        solution = Solution()
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)

        self.assertEqual(solution.smallestFromLeaf(root), 'dba')


if __name__ == '__main__':
    unittest.main()
