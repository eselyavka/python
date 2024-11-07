import heapq
import unittest


class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        for idx, t in enumerate(tasks):
            t.append(idx)

        tasks.sort(key=lambda t: t[0])

        ans, h = [], []
        i, time = 0, tasks[0][0]

        while h or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(h, [tasks[i][1], tasks[i][2]])
                i += 1
            if h:
                t = heapq.heappop(h)
                time += t[0]
                ans.append(t[1])
            else:
                time = tasks[i][0]

        return ans


class TestSolution(unittest.TestCase):
    def test_getOrder(self):
        solution = Solution()
        self.assertListEqual(solution.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]), [0, 2, 3, 1])


if __name__ == '__main__':
    unittest.main()
