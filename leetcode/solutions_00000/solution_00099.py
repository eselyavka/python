import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        arr = []
        curr = root
        stack = []

        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                node = stack.pop()
                arr.append(node.val)
                curr = node.right
            else:
                break

        sorted_arr = sorted(arr)
        n = len(arr)

        swap_from, swap_to = None, None
        for i in range(n):
            if arr[i] != sorted_arr[i]:
                swap_from = sorted_arr[i]
                swap_to = arr[i]

        q = [root]
        while q:
            node = q.pop()

            if node.val == swap_to:
                node.val = swap_from
            elif node.val == swap_from:
                node.val = swap_to

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


class TestSolution(unittest.TestCase):
    def test_recoverTree(self):
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.left.right = TreeNode(2)

        solution = Solution()
        solution.recoverTree(root)

        arr = []
        curr = root
        stack = []

        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                node = stack.pop()
                arr.append(node.val)
                curr = node.right
            else:
                break

        self.assertListEqual(arr, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
