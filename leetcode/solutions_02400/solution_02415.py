import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def invert(root1, root2, level):
            if not root1 or not root2:
                return None

            if level % 2 == 0:
                temp = root2.val
                root2.val = root1.val
                root1.val = temp

            invert(root1.left, root2.right, level + 1)
            invert(root1.right, root2.left, level + 1)

        if root.left and root.right:
            invert(root.left, root.right, 0)

        return root


class TestSolution(unittest.TestCase):
    def test_reverseOddLevels(self):
        solution = Solution()

        root = TreeNode(2)
        root.left = TreeNode(3)
        root.right = TreeNode(5)
        root.left.left = TreeNode(8)
        root.left.right = TreeNode(13)
        root.right.left = TreeNode(21)
        root.right.right = TreeNode(34)

        reversed_root = solution.reverseOddLevels(root)

        ans = []
        q = [reversed_root]
        while q:
            node = q.pop(0)
            ans.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        self.assertListEqual(ans, [2, 5, 3, 8, 13, 21, 34])


if __name__ == '__main__':
    unittest.main()
