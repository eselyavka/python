import unittest

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = [root]

        ans = []
        d = 0

        while q:
            i = len(q)
            buf = []
            while i > 0:
                node = q.pop(0)
                if d % 2 == 1:
                    buf.insert(0, node.val)
                else:
                    buf.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                i -= 1

            d += 1
            ans.append(buf)

        return ans


class TestSolution(unittest.TestCase):
    def test_zigzagLevelOrder(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        solution = Solution()

        self.assertListEqual(solution.zigzagLevelOrder(root), [[3], [20, 9], [15, 7]])


if __name__ == '__main__':
    unittest.main()