#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

class TestSolution(unittest.TestCase):

    def list_to_array(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        return arr

    def test_deleteNode(self):
        solution = Solution()
        head = ListNode(4)
        head.next = ListNode(5)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(9)

        solution.deleteNode(head.next)
        self.assertListEqual(self.list_to_array(head), [4, 1, 9])

if __name__ == '__main__':
    unittest.main()
