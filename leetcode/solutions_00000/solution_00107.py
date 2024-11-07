#!/usr/bin/env python

import unittest
from collections import deque


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            tmp = []
            data = []
            while stack:
                node = stack.pop(0)
                data.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            res.insert(0, data)
            stack = tmp

        return res


class Solution2(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = deque()
        q.appendleft(root)
        res = []  # or create one more deque and appendleft
        while q:
            size = len(q)
            acc = []
            while size:
                node = q.pop()
                acc.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
                size -= 1
            res.append(acc)

        res.reverse()

        return res


class TestSolution(unittest.TestCase):

    def test_levelOrderBottom(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        solution = Solution()

        self.assertListEqual(solution.levelOrderBottom(root),
                             [[15, 7], [9, 20], [3]])

        solution2 = Solution2()

        self.assertListEqual(solution2.levelOrderBottom(root),
                             [[15, 7], [9, 20], [3]])


if __name__ == '__main__':
    unittest.main()
