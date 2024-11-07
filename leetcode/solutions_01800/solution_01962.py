import heapq
import unittest


class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """

        arr = [-x for x in piles]
        heapq.heapify(arr)

        while k > 0:
            pile = heapq.heappop(arr)
            pile += -pile // 2
            heapq.heappush(arr, pile)
            k -= 1

        return -sum(arr)


class TestSolution(unittest.TestCase):
    def test_minStoneSum(self):
        solution = Solution()
        self.assertEqual(solution.minStoneSum([5, 4, 9], 2), 12)


if __name__ == '__main__':
    unittest.main()
