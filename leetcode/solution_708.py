#!/usr/bin/env python

import unittest


class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """

        if not head:
            singular = Node(insertVal)
            singular.next = singular
            return singular

        curr, prev = head.next, head

        done = False
        while curr != head:
            if prev.val <= insertVal <= curr.val:
                done = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    done = True

            if done:
                prev.next = Node(insertVal, curr)
                return head

            prev, curr = curr, curr.next

        prev.next = Node(insertVal, curr)

        return head

class TestSolution(unittest.TestCase):

    def test_insert(self):
        head = Node(3)
        head.next = Node(4)
        head.next.next = Node(1)
        head.next.next.next = head

        solution = Solution()
        _ = solution.insert(head, 2)

        arr = []
        curr, prev = head.next, head

        while curr != head:
            arr.append(prev.val)
            prev, curr = curr, curr.next

        arr.append(prev.val)

        self.assertListEqual(arr, [3, 4, 1, 2])


if __name__ == '__main__':
    unittest.main()
