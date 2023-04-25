import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_nodes = 0
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def rec(root, left, steps):
            if not root:
                self.max_nodes = max(self.max_nodes, steps - 1)
                return

            if left:
                rec(root.left, False, steps + 1)
                rec(root.right, True, 1)
            else:
                rec(root.left, False, 1)
                rec(root.right, True, steps + 1)

        rec(root, False, 0)
        rec(root, True, 0)

        return self.max_nodes


class TestSolution(unittest.TestCase):
    def test_longestZigZag(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.left.right = TreeNode(1)
        root.left.right.left = TreeNode(1)
        root.left.right.left.right = TreeNode(1)
        root.left.right.right = TreeNode(1)
        root.right = TreeNode(1)

        self.assertEqual(solution.longestZigZag(root), 4)


if __name__ == '__main__':
    unittest.main()
