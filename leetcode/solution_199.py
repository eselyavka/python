#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root

        s, res = [root], []

        while s:
            res.append(s[-1].val)
            level = []
            while s:
                node = s.pop(0)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            if level:
                s.extend(level)

        return res


class TestSolution(unittest.TestCase):

    def test_rightSideView(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)

        solution = Solution()

        self.assertListEqual(solution.rightSideView(root), [1, 3, 4])


if __name__ == '__main__':
    unittest.main()
