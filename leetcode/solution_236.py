#!/usr/bin/env python
import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def rec(node):
            if not node:
                return 0, None

            left_res = rec(node.left)
            if left_res[0] == 2:
                return left_res

            right_res = rec(node.right)

            if right_res[0] == 2:
                return right_res

            res = left_res[0] + right_res[0] + (node == p) + (node == q)

            return res, node if res == 2 else None

        res = rec(root)

        return res[1]


class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ppath = []
        qpath = []
        paths = []

        def rec(root, node, path):
            if not root:
                return

            path.append(root)

            if root == node:
                paths.append(path[:])
                return

            rec(root.left, node, path)
            rec(root.right, node, path)

            path.pop()

        rec(root, p, ppath)
        rec(root, q, qpath)

        n = len(paths[0])
        m = len(paths[1])

        i, j = 0, 0

        while i < n and j < m:
            if paths[0][i] != paths[1][j]:
                return paths[0][i-1]

            i += 1
            j += 1

        if i < n:
            return paths[0][i-1]

        if j < m:
            return paths[1][j-1]


class TestSolution(unittest.TestCase):
    def test_lowestCommonAncestor(self):
        solution = Solution()
        solution2 = Solution2()

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        actual = solution.lowestCommonAncestor(root, root.left, root.right)

        self.assertEqual([actual.val,
                          actual.left.val,
                          actual.right.val], [1, 2, 3])

        actual = solution2.lowestCommonAncestor(root, root.left, root.right)

        self.assertEqual([actual.val,
                          actual.left.val,
                          actual.right.val], [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
