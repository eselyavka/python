import unittest
from collections import deque


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return root

        q = deque([root])

        while q:
            cnt = len(q)
            arr = []
            while cnt > 0:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                arr.append(node)

                cnt -= 1

            for i in range(1, len(arr)):
                arr[i - 1].next = arr[i]

        return root


class TestSolution(unittest.TestCase):
    def test_connect(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right = Node(3)
        root.right.right = Node(7)

        solution = Solution()

        _ = solution.connect(root)

        ans = []
        q = deque([root])
        while q:
            node = q.popleft()
            ans.append(node.next.val if node.next else None)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        self.assertListEqual(ans, [None, 3, None, 5, 7, None])


if __name__ == '__main__':
    unittest.main()
