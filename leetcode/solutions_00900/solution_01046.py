import heapq
import unittest


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        negative_stones = [-x for x in stones]
        heapq.heapify(negative_stones)

        while len(negative_stones) != 1:
            x = -heapq.heappop(negative_stones)
            y = -heapq.heappop(negative_stones)
            res = abs(x - y)
            heapq.heappush(negative_stones, -res)

        ans = -negative_stones[0]

        return ans


class TestSolution(unittest.TestCase):
    def test_lastStoneWeight(self):
        solution = Solution()
        self.assertEqual(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)


if __name__ == '__main__':
    unittest.main()
