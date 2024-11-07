import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        curr = root
        stack = []
        flag = False

        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                if flag:
                    return stack[-1]
                node = stack.pop()
                if node == p:
                    flag = True
                curr = node.right
            else:
                break


class TestSolution(unittest.TestCase):
    def test_inorderSuccessor(self):
        solution = Solution()
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        actual = solution.inorderSuccessor(root, root.left)
        self.assertIsNotNone(actual)
        self.assertEqual(actual.val, 2)


if __name__ == '__main__':
    unittest.main()
