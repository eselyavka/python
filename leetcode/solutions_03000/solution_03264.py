import heapq
import unittest


class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """

        n = len(nums)
        res = [-1] * n

        heap = []
        for idx, num in enumerate(nums):
            heapq.heappush(heap, (num, idx))

        for _ in range(k):
            curr, idx = heapq.heappop(heap)
            heapq.heappush(heap, (curr * multiplier, idx))

        for num, idx in heap:
            res[idx] = num

        return res


class TestSolution(unittest.TestCase):
    def test_getFinalState(self):
        solution = Solution()
        self.assertListEqual(solution.getFinalState([2, 1, 3, 5, 6], 5, 2), [8, 4, 6, 5, 6])


if __name__ == '__main__':
    unittest.main()
