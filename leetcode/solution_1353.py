import heapq
import unittest


class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """

        events.sort(key=lambda t: (t[0], t[1]), reverse=True)

        h = []
        day = 0
        ans = 0

        while h or events:
            if not h:
                day = events[-1][0]

            while events and day >= events[-1][0]:
                heapq.heappush(h, events.pop()[1])

            heapq.heappop(h)

            ans += 1
            day += 1

            while h and day > h[0]:
                heapq.heappop(h)

        return ans


class TestSolution(unittest.TestCase):
    def test_maxEvents(self):
        solution = Solution()
        self.assertEqual(solution.maxEvents([[1, 2], [2, 3], [3, 4]]), 3)


if __name__ == '__main__':
    unittest.main()
