#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.idx = 0


    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def construct_tree(preorder, data, min_, max_):
            if self.idx < len(preorder):
                if preorder[self.idx] > min_ and preorder[self.idx] < max_:
                    node = TreeNode(preorder[self.idx])
                    self.idx += 1
                    if self.idx < len(preorder):
                        node.left = construct_tree(preorder, preorder[self.idx], min_, data)
                    if self.idx < len(preorder):
                        node.right = construct_tree(preorder, preorder[self.idx], data, max_)
                    return node

            return None

        return construct_tree(preorder, preorder[0], float('-inf'), float('+inf'))


class TestSolution(unittest.TestCase):

    def test_bstFromPreorder(self):
        solution = Solution()

        root = solution.bstFromPreorder([4, 2])

        self.assertEqual([root.val, root.left.val], [4, 2])


if __name__ == '__main__':
    unittest.main()
