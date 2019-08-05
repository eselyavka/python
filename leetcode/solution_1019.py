#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        res = [0] * len(arr)
        s = []
        for i in range(len(arr)):
            next_ = arr[i]
            if s:
                while s and s[-1][0] < next_:
                    _, idx = s.pop()
                    res[idx] = next_
            s.append((next_, i))
        return res

class TestSolution(unittest.TestCase):

    def test_nextLargerNodes(self):
        solution = Solution()

        head = ListNode(2)
        head.next = ListNode(1)
        head.next.next = ListNode(5)

        self.assertListEqual(solution.nextLargerNodes(head), [5, 5, 0])

        head = ListNode(2)
        head.next = ListNode(7)
        head.next.next = ListNode(4)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(5)

        self.assertListEqual(solution.nextLargerNodes(head), [7, 0, 5, 5, 0])

        head = ListNode(1)
        head.next = ListNode(7)
        head.next.next = ListNode(5)
        head.next.next.next = ListNode(1)
        head.next.next.next.next = ListNode(9)
        head.next.next.next.next.next = ListNode(2)
        head.next.next.next.next.next.next = ListNode(5)
        head.next.next.next.next.next.next.next = ListNode(1)

        self.assertListEqual(solution.nextLargerNodes(head), [7, 9, 9, 9, 0, 5, 0, 0])

        head = ListNode(9)
        head.next = ListNode(7)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(7)
        head.next.next.next.next = ListNode(6)
        head.next.next.next.next.next = ListNode(9)

        self.assertListEqual(solution.nextLargerNodes(head), [0, 9, 7, 9, 9, 0])

if __name__ == '__main__':
    unittest.main()
