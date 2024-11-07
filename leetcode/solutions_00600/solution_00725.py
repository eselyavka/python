#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            return [None] * k

        list_head = list_iter = root
        size = 0
        while list_iter:
            size += 1
            list_iter = list_iter.next

        res = []
        if size <= k:
            while list_head:
                buf = list_head.next
                list_head.next = None
                res.append(list_head)
                list_head = buf

            for _ in range(k-size):
                res.append(None)
        else:
            bucket = size // k
            addition = size % k
            while list_head:
                n = bucket + (1 if addition > 1 else max(addition, 0))
                split_head = split_iter = list_head
                res.append(split_head)
                while n - 1:
                    list_head = list_head.next
                    split_iter = split_iter.next
                    n -= 1

                buf = split_iter.next
                split_iter.next = None
                list_head = buf
                addition -= 1

        return res


class TestSolution(unittest.TestCase):

    def list_to_list(self, arr):
        actual = []
        for item in arr:
            buf = []
            while item:
                buf += [item.val]
                item = item.next
            actual.append(buf)

        return actual

    def test_splitListToParts(self):
        solution = Solution()

        lst = ListNode(1)
        lst.next = ListNode(2)
        lst.next.next = ListNode(3)

        actual = self.list_to_list(solution.splitListToParts(lst, 5))
        self.assertEqual(actual, [[1], [2], [3], [], []])


if __name__ == '__main__':
    unittest.main()
