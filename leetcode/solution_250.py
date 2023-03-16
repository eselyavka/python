import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.ans = 0

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def rec(node):
            if node is None:
                return True

            left = rec(node.left)
            right = rec(node.right)

            if not left or not right:
                return False

            if node.left and node.left.val != node.val:
                return False

            if node.right and node.right.val != node.val:
                return False

            self.ans += 1

            return True

        rec(root)

        return self.ans


class TestSolution(unittest.TestCase):
    def test_countUnivalSubtrees(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(5)

        root.left.left = TreeNode(5)
        root.left.right = TreeNode(5)

        root.right.right = TreeNode(5)

        solution = Solution()
        self.assertEqual(solution.countUnivalSubtrees(root), 4)


if __name__ == '__main__':
    unittest.main()
