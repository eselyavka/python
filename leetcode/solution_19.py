#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        arr = []

        while head:
            arr.append(head)
            head = head.next

        if len(arr) == 1:
            return None

        if n == len(arr):
            return arr[1]
        elif n == 1:
            arr[-(n+1)].next = None
        else:
            arr[-(n+1)].next = arr[-(n-1)]

        return arr[0]

class TestSolution(unittest.TestCase):

    def list_traversals(self, head):
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        return arr

    def test_removeNthFromEnd(self):
        solution = Solution()

        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(3)
        node.next.next.next = ListNode(4)
        node.next.next.next.next = ListNode(5)

        actual = solution.removeNthFromEnd(node, 2)

        self.assertListEqual(self.list_traversals(actual), [1, 2, 3, 5])

if __name__ == '__main__':
    unittest.main()
