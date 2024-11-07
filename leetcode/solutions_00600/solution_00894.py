#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []

        mem = {0: [], 1: [TreeNode(0)]}

        if mem.get(N):
            return mem[N]

        def rec(n):
            if n not in mem:
                res = []
                for i in range(1, n-1, 2):
                    for left in rec(i):
                        for right in rec(n-i-1):
                            tmp = TreeNode(0)
                            tmp.left = left
                            tmp.right = right
                            res.append(tmp)
                mem[n] = res

            return mem[n]

        res = rec(N)

        return res


class TestSolution(unittest.TestCase):

    def test_allPossibleFBT(self):
        solution = Solution()
        res = solution.allPossibleFBT(3)

        def flatten(tree_it):
            res = []
            for tree in tree_it:
                stack = [tree]
                buf = []
                while stack:
                    size = len(stack)
                    while size:
                        node = stack.pop()
                        buf.append(node.val)

                        if node.left:
                            stack.append(node.left)
                        if node.right:
                            stack.append(node.right)

                        size -= 1
                res.append(buf)

            return res

        self.assertEqual(flatten(res), [[0, 0, 0]])


if __name__ == '__main__':
    unittest.main()
