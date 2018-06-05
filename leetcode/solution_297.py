#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Codec(object):

    def reconstruct_preorder(self, data):
        it = iter(data.split(chr(9)))
        def reconstruct_preorder_helper():
            subtree_key = None
            try:
                subtree_key = next(it)
            except StopIteration:
                pass

            if subtree_key is None or subtree_key == chr(0):
                return

            root = TreeNode(subtree_key)
            root.left = reconstruct_preorder_helper()
            root.right = reconstruct_preorder_helper()
            return root

        return reconstruct_preorder_helper()

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return

        def preOrder(root):
            if root:
                vals.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
            else:
                vals.append(chr(0))

        vals = []
        preOrder(root)

        return chr(9).join(vals)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        return self.reconstruct_preorder(data)

class TestSolution(unittest.TestCase):

    def _helper(self, root):
        def preorder(root):
            if root:
                arr.append(root.val)
                arr.append(preorder(root.left))
                arr.append(preorder(root.right))

        arr = []
        preorder(root)

        return arr

    def test_codec(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(16)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(11)

        root2 = TreeNode(3)
        root2.left = TreeNode(2)
        root2.left.left = TreeNode(1)
        root2.left.right = None
        root2.right = TreeNode(4)

        root3 = TreeNode(10)

        root4 = TreeNode(0)
        root4.left = TreeNode(-1)

        root5 = TreeNode(0)
        root5.right = TreeNode(100)

        root6 = TreeNode(5)
        root6.left = TreeNode(1)
        root6.left.right = TreeNode(2)
        root6.left.right.left = TreeNode(0)
        root6.right = TreeNode(16)
        root6.right.left = TreeNode(4)
        root6.right.right = TreeNode(11)

        root7 = TreeNode(0)

        root8 = TreeNode(1)
        root8.left = TreeNode(2)
        root8.right = TreeNode(3)
        root8.right.left = TreeNode(4)
        root8.right.right = TreeNode(5)

        solution = Codec()

        self.assertEqual(
            [x for x in self._helper(solution.deserialize(
                solution.serialize(root))) if x is not None],
            ['5', '1', '16', '4', '11'])

        self.assertIsNone(solution.deserialize(solution.serialize(None)))

        self.assertEqual(
            [x for x in self._helper(solution.deserialize(
                solution.serialize(root2))) if x is not None],
            ['3', '2', '1', '4'])

        self.assertEqual(
            [x for x in self._helper(solution.deserialize(
                solution.serialize(root3))) if x is not None],
            ['10'])

        self.assertEqual(
            [x for x in self._helper(
                solution.deserialize(solution.serialize(root4))) if x is not None],
            ['0', '-1'])

        self.assertEqual(
            [x for x in self._helper(
                solution.deserialize(solution.serialize(root5))) if x is not None],
            ['0', '100'])

        self.assertEqual(
            [x for x in self._helper(
                solution.deserialize(solution.serialize(root6))) if x is not None],
            ['5', '1', '2', '0', '16', '4', '11'])

        self.assertEqual(
            [x for x in self._helper(
                solution.deserialize(solution.serialize(root7))) if x is not None],
            ['0'])

        self.assertEqual(
            [x for x in self._helper(
                solution.deserialize(solution.serialize(root8))) if x is not None],
            ['1', '2', '3', '4', '5'])

if __name__ == '__main__':
    unittest.main()
