#!/usr/bin/env python

import unittest


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        arr1, arr2 = [], []

        def rec(root, arr):
            if not root:
                return

            rec(root.left, arr)
            arr.append(root.val)
            rec(root.right, arr)

        rec(root1, arr1)
        rec(root2, arr2)

        res = []

        def merge_sort(arr1, arr2):
            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                elif arr1[i] > arr2[j]:
                    res.append(arr2[j])
                    j += 1
                else:
                    res.extend([arr1[i], arr2[j]])
                    i += 1
                    j += 1

            res.extend(arr1[i:])
            res.extend(arr2[j:])

        merge_sort(arr1, arr2)

        return res


class TestSolution(unittest.TestCase):
    def test_getAllElements(self):
        root1 = Node(2)
        root1.left = Node(1)
        root1.right = Node(4)

        root2 = Node(1)
        root2.left = Node(0)
        root2.right = Node(3)

        solution = Solution()
        self.assertListEqual(
            solution.getAllElements(root1, root2),
            [0, 1, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
