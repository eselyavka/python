#!/usr/bin/env python

import unittest


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = 0

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rec(node):
            if not node:
                return 0

            left = rec(node.left)

            right = rec(node.right)

            self.res += abs(left) + abs(right)

            return node.val + left + right - 1

        rec(root)

        return self.res


class TestSolution(unittest.TestCase):
    def test_distributeCoins(self):
        root = Node(3)
        root.left = Node(0)
        root.right = Node(0)

        solution = Solution()
        self.assertEqual(solution.distributeCoins(root), 2)


if __name__ == '__main__':
    unittest.main()
