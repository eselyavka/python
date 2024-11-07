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


class Solution2(object):
    def mergeArrays(self, arr1, arr2, n1, n2):
        arr3 = [None] * (n1 + n2)
        i = 0
        j = 0
        k = 0

        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                arr3[k] = arr1[i]
                k = k + 1
                i = i + 1
            else:
                arr3[k] = arr2[j]
                k = k + 1
                j = j + 1

        while i < n1:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1

        while j < n2:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1

        return arr3

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        res = []
        while True:
            buf = []
            for i in range(len(lists)):
                if lists[i]:
                    buf.append(lists[i].val)
                    lists[i] = lists[i].next
            if not res:
                res = sorted(buf)
            else:
                res = self.mergeArrays(res, sorted(buf), len(res), len(buf))
            is_empty = any(lists)
            if not is_empty:
                break

        fake_head = head = ListNode('fake')
        for num in res:
            head.next = ListNode(num)
            head = head.next

        return fake_head.next


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

        solution2 = Solution2()
        head = solution2.mergeKLists([lst, lst2, lst3])
        actual = []
        while head:
            actual.append(head.val)
            head = head.next

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
