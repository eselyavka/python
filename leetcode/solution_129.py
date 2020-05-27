#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        acc = []

        def rec(root, path, pathLen):
            if not root:
                return

            if len(path) > pathLen:
                path[pathLen] = str(root.val)
            else:
                path.append(str(root.val))

            pathLen += 1

            if root.left is None and root.right is None:
                acc.append(int(''.join(path[:pathLen])))
            else:
                rec(root.left, path, pathLen)
                rec(root.right, path, pathLen)

        path = []
        rec(root, path, 0)

        return sum(acc)


class Solution2(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def root_to_leaf_pathes(d, child):
            q = [child]
            while True:
                parent = d.get(q[0])
                if not parent:
                    break
                q.insert(0, parent)

            res = int(''.join([str(n.val) for n in q]))

            return res

        stack, parent = [root], {}
        parent[root] = None
        sum_ = 0

        while stack:

            node = stack.pop()

            if node.left is None and node.right is None:
                sum_ += root_to_leaf_pathes(parent, node)

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        return sum_


class TestSolution(unittest.TestCase):

    def test_sumNumbers(self):
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)

        solution = Solution()

        self.assertEqual(solution.sumNumbers(root), 1026)

        solution2 = Solution2()
        self.assertEqual(solution2.sumNumbers(root), 1026)


if __name__ == '__main__':
    unittest.main()
