#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = None


class Solution(object):
    def __init__(self):
        self.max = 0

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return self.max

        def rec(root, level):
            self.max = max(self.max, level)
            if not root:
                return

            if not root.children:
                return

            for node in root.children:
                rec(node, level + 1)

        rec(root, 1)

        return self.max


class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        s = [root]
        res = 0

        while s:
            cnt = len(s)
            while cnt > 0:
                node = s.pop(0)
                if node and node.children:
                    s.extend(node.children)
                cnt -= 1
            res += 1

        return res


class TestSolution(unittest.TestCase):

    def test_maxDepth(self):
        root = TreeNode(1)
        child = TreeNode(3)
        root.children = [child, TreeNode(2), TreeNode(4)]
        child.children = [TreeNode(5), TreeNode(6)]

        solution = Solution()

        self.assertEqual(solution.maxDepth(root), 3)

        solution = Solution()
        self.assertEqual(solution.maxDepth(None), 0)

        solution = Solution2()

        self.assertEqual(solution.maxDepth(root), 3)
        self.assertEqual(solution.maxDepth(None), 0)


if __name__ == '__main__':
    unittest.main()
