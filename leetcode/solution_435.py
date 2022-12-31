import unittest


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        if n == 1:
            return 0

        intervals.sort(key=lambda i: i[0])
        prev_end = intervals[0][1]
        ans = 0

        for i in range(1, n):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            if prev_end > curr_start:
                prev_end = min(prev_end, curr_end)
                ans += 1
            else:
                prev_end = curr_end

        return ans


class TestSolution(unittest.TestCase):
    def test_eraseOverlapIntervals(self):
        solution = Solution()
        self.assertEqual(solution.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]), 2)


if __name__ == '__main__':
    unittest.main()
