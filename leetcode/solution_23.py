#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for list_ in lists:
            while list_:
                heap.append(list_.val)
                list_ = list_.next

        head = node = ListNode('head')
        for val in sorted(heap):
            node.next = ListNode(val)
            node = node.next

        return head.next


class TestSolution(unittest.TestCase):

    def test_mergeKLists(self):
        lst = ListNode(1)
        lst.next = ListNode(4)
        lst.next.next = ListNode(5)

        lst2 = ListNode(1)
        lst2.next = ListNode(3)
        lst2.next.next = ListNode(4)

        lst3 = ListNode(2)
        lst3.next = ListNode(6)

        solution = Solution()
        expected = [1, 1, 2, 3, 4, 4, 5, 6]

        head = solution.mergeKLists([lst, lst2, lst3])
        actual = []
        while head:
            actual.append(head.val)
            head = head.next

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
