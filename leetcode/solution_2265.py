import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def subtree(node):
            if not node:
                return 0, 0

            cleft, sleft = subtree(node.left)
            cright, sright = subtree(node.right)

            c = cleft + cright
            s = sleft + sright

            return 1 + c, node.val + s

        q = [root]

        ans = 0

        while q:
            node = q.pop()

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

            c, s = subtree(node)

            if node.val == s // c:
                ans += 1

        return ans


class TestSolution(unittest.TestCase):
    def test_averageOfSubtree(self):
        root = TreeNode(4)
        root.left = TreeNode(8)
        root.right = TreeNode(5)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(1)
        root.right.right = TreeNode(6)

        solution = Solution()
        actual = solution.averageOfSubtree(root)

        self.assertEqual(actual, 5)


if __name__ == '__main__':
    unittest.main()
