import unittest
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = deque()
        q.append(root)

        ans = 0
        while q:
            size = len(q)
            arr = []
            while size > 0:
                node = q.popleft()

                arr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1

            n = len(arr)
            if n > 1:
                visited = [False] * n
                index_arr = [(value, index) for index, value in enumerate(arr)]
                index_arr.sort(key=lambda x: x[0])

                for i in range(n):
                    if visited[i] or index_arr[i][1] == i:
                        continue
                    cycles = 0
                    j = i

                    while not visited[j]:
                        visited[j] = True
                        j = index_arr[j][1]
                        cycles += 1
                    if cycles > 1:
                        ans += cycles - 1
        return ans


class TestSolution(unittest.TestCase):
    def test_minimumOperations(self):
        solution = Solution()

        root = TreeNode(1)
        root.left = TreeNode(4)
        root.right = TreeNode(3)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(6)
        root.right.left = TreeNode(8)
        root.right.right = TreeNode(5)
        root.right.left.left = TreeNode(9)
        root.right.right.left = TreeNode(10)

        ans = solution.minimumOperations(root)

        self.assertEqual(ans, 3)


if __name__ == '__main__':
    unittest.main()
