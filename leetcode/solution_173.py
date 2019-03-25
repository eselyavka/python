import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = list()

        def rec(root):
            if not root:
                return
            rec(root.right)
            self.s.append(root.val)
            rec(root.left)

        rec(root)


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.s.pop()


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.s) > 0


class TestSolution(unittest.TestCase):
    def test_BSTIterator(self):
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(20)

        iterator = BSTIterator(root)
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 7)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 9)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 15)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 20)
        self.assertFalse(iterator.hasNext())


if __name__ == '__main__':
    unittest.main()
