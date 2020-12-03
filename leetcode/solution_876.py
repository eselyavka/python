#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size, _head = 0, head

        while head:
            size += 1
            head = head.next

        if size == 1:
            return _head

        i = 0
        while _head:
            if i == size // 2:
                return _head
            _head = _head.next
            i += 1


class Solution2(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


class TestSolution(unittest.TestCase):

    def test_middleNode(self):
        solution = Solution()
        solution2 = Solution()

        lst = ListNode(1)
        lst.next = ListNode(2)
        lst.next.next = ListNode(6)
        lst.next.next.next = ListNode(3)
        lst.next.next.next.next = ListNode(4)
        lst.next.next.next.next.next = ListNode(5)
        lst.next.next.next.next.next.next = ListNode(6)

        self.assertEqual(solution.middleNode(lst).val, 3)
        self.assertEqual(solution2.middleNode(lst).val, 3)

        lst = ListNode(1)

        self.assertEqual(solution.middleNode(lst).val, 1)
        self.assertEqual(solution2.middleNode(lst).val, 1)


if __name__ == '__main__':
    unittest.main()
