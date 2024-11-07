#!/usr/bin/env python

import unittest
from collections import defaultdict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = defaultdict(list)

        def dfs(root, x, y):
            if not root:
                return

            d[x].append(root)
            root.y = y
            dfs(root.left, x-1, y-1)
            dfs(root.right, x+1, y-1)

        dfs(root, 0, 0)

        def my_cmp(left, right):
            if left.y > right.y:
                return 1
            elif left.y < right.y:
                return -1
            else:
                if left.val > right.val:
                    return -1
                elif left.val < right.val:
                    return 1
                return 0

        res = [[node.val for node in sorted(t[1], cmp=my_cmp, reverse=True)] for t in sorted(d.items(), key=lambda x: x[0])]

        return res


class TestSolution(unittest.TestCase):
    def test_verticalTraversal(self):
        solution = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertListEqual(solution.verticalTraversal(root), [[9], [3, 15], [20], [7]])


if __name__ == '__main__':
    unittest.main()
