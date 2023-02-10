import heapq
import unittest


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)

        h = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(h, -matrix[i][j])
                if len(h) > k:
                    heapq.heappop(h)

        return -h[0]


class TestSolution(unittest.TestCase):
    def test_kthSmallest(self):
        solution = Solution()
        self.assertEqual(solution.kthSmallest([[1, 5, 9],
                                               [10, 11, 13],
                                               [12, 13, 15]], 8), 13)


if __name__ == '__main__':
    unittest.main()
