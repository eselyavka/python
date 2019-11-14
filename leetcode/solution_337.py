#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.dfs(root))

    def dfs(self, root):
        if not root:
            return [0, 0]

        res = [0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        res[0] = root.val + left[1] + right[1]
        res[1] = max(left[0], left[1]) + max(right[0], right[1])

        return res


class Solution2(object):
    def dfs(self, root, is_parent_taken, mem):
        if not root:
            return 0

        if is_parent_taken:
            sum_left = mem.get((root.left, False), 0) or self.dfs(root.left, False, mem)
            sum_right = mem.get((root.right, False), 0) or self.dfs(root.right, False, mem)
            mem[(root, is_parent_taken)] = sum_left + sum_right

            return sum_left + sum_right

        s1 = mem.get((root.left, False), 0) or self.dfs(root.left, False, mem)
        s2 = mem.get((root.right, False), 0) or self.dfs(root.right, False, mem)
        s3 = mem.get((root.left, True), 0) or self.dfs(root.left, True, mem)
        s4 = mem.get((root.right, True), 0) or self.dfs(root.right, True, mem)

        max_ = max(s1+s2, root.val + s3+s4)

        mem[(root, is_parent_taken)] = max_

        return max_

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mem = dict()

        return self.dfs(root, False, mem)


class TestSolution(unittest.TestCase):

    def test_rob(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(3)
        root.right.right = TreeNode(1)

        root2 = TreeNode(3)
        root2.left = TreeNode(4)
        root2.right = TreeNode(5)
        root2.left.left = TreeNode(1)
        root2.left.right = TreeNode(3)
        root2.right.right = TreeNode(1)

        solution, solution2 = Solution(), Solution2()

        self.assertEqual(solution.rob(root), 7)
        self.assertEqual(solution.rob(root2), 9)

        self.assertEqual(solution2.rob(root), 7)
        self.assertEqual(solution2.rob(root2), 9)


if __name__ == '__main__':
    unittest.main()
