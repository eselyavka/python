#!/usr/bin/env python

import unittest
from collections import deque, defaultdict


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
            k = len(s)
            for _ in range(k):
                node = s.pop(0)
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)

        return res


class Solution2(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        q = deque([(root, 0)])

        level_traversals = defaultdict(list)

        while q:
            node, level = q.popleft()
            level_traversals[level].append(node.val)

            if node.left:
                q.append((node.left, level+1))

            if node.right:
                q.append((node.right, level+1))

        res = []

        for item in sorted(level_traversals.keys()):
            res.append(level_traversals[item][-1])

        return res


class TestSolution(unittest.TestCase):
    def test_rightSideView(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)

        solution = Solution()
        solution2 = Solution2()

        self.assertListEqual(solution.rightSideView(root), [1, 3, 4])
        self.assertListEqual(solution2.rightSideView(root), [1, 3, 4])


if __name__ == '__main__':
    unittest.main()
