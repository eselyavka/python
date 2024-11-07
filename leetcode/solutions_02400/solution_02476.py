import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        curr = root
        s = []
        inorder = []
        while True:
            if curr is not None:
                s.append(curr)
                curr = curr.left
            elif s:
                node = s.pop()
                inorder.append(node.val)
                curr = node.right
            else:
                break

        def find_closest(target, arr):
            if target < arr[0]:
                return -1, arr[0]
            if target > arr[-1]:
                return arr[-1], -1
            r = 0
            l = len(arr)
            mid = 0
            while r < l:
                mid = (r + l) // 2
                if arr[mid] == target:
                    return target, target

                if target < arr[mid]:
                    if mid > 0 and target > arr[mid - 1]:
                        return arr[mid - 1], arr[mid]
                    l = mid
                else:
                    if mid < len(arr) - 1 and target < arr[mid + 1]:
                        return arr[mid], arr[mid + 1]
                    r = mid + 1

        ans = []
        for q in queries:
            ans.append(list(find_closest(q, inorder)))

        return ans


class TestSolution(unittest.TestCase):
    def test_closestNodes(self):
        solution = Solution()
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.right = TreeNode(13)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(15)
        root.right.right.left = TreeNode(14)

        self.assertListEqual(solution.closestNodes(root, [2, 5, 16]), [[2, 2], [4, 6], [15, -1]])


if __name__ == '__main__':
    unittest.main()
