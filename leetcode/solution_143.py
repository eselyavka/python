#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        arr = []
        while head:
            arr.append(head)
            head = head.next

        left, right, res = 0, len(arr) - 1, []

        while left <= right:
            if left == right:
                res.append(arr[left])
            else:
                res.append(arr[left])
                res.append(arr[right])
            left += 1
            right -= 1

        for i in range(1, len(res)):
            res[i-1].next = res[i]

        res[-1].next = None

class TestSolution(unittest.TestCase):

    def list_traversals(self, head):
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        return arr

    def test_reorderList(self):
        solution = Solution()

        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(3)
        node.next.next.next = ListNode(4)

        solution.reorderList(node)

        self.assertListEqual(self.list_traversals(node), [1, 4, 2, 3])

if __name__ == '__main__':
    unittest.main()
