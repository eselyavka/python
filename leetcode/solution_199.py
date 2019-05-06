#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root
        s = [root]
        res = []
        while s:
            test = []
            while s:
                node=s.pop(0)
                print node.val
                if node.left:
                    test.append(node.left)
                if node.right:
                    test.append(node.right)
            if test:
                res.append(test[-1].val)
            #print [x.val for x in test]
            s.extend(test)
        return [root.val] + res


class TestSolution(unittest.TestCase):

    def test_rightSideView(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)

        solution = Solution()

        self.assertListEqual(solution.rightSideView(root), [1, 3, 4])

if __name__ == '__main__':
    unittest.main()
