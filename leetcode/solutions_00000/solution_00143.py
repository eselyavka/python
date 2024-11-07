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


class Solution2(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            next_=second.next
            second.next = prev
            prev = second
            second = next_

        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


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

        solution2 = Solution2()
        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(3)
        node.next.next.next = ListNode(4)
        node.next.next.next.next = ListNode(5)

        solution2.reorderList(node)

        self.assertListEqual(self.list_traversals(node), [1, 5, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()
