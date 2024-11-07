import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        arr = []
        it = head
        while it:
            next_ = it.next
            it.next = None
            arr.append(it)
            it = next_

        for i in range(1, len(arr), 2):
            arr[i - 1], arr[i] = arr[i], arr[i - 1]

        new_head = ListNode(-1)
        tail = new_head

        for node in arr:
            tail.next = node
            tail = tail.next

        return new_head.next


class TestSolution(unittest.TestCase):
    def test_swapPairs(self):
        solution = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)

        actual = solution.swapPairs(head)

        ans = []
        while actual:
            ans.append(actual.val)
            actual = actual.next

        self.assertListEqual(ans, [2, 1, 4, 3])


if __name__ == '__main__':
    unittest.main()
