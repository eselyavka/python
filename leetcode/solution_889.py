#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre and not post:
            return None

        root = TreeNode(pre[0])
        if len(post) == 1:
            return root

        idx = pre.index(post[-2])

        root.left = self.constructFromPrePost(pre[1:idx], post[:idx-1])
        root.right = self.constructFromPrePost(pre[idx:], post[idx - 1: -1])

        return root

class TestSolution(unittest.TestCase):

    def test_constructFromPrePost(self):

        actual = []
        solution = Solution()

        def level(root):
            s = [root]
            while s:
                node = s.pop(0)
                actual.append(node.val)

                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)

        level(solution.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]))

        self.assertListEqual(actual, [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()
