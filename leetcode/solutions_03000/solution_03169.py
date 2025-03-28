import unittest


class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort(key=lambda t: t[0])

        merged_meetings = []
        start, end = meetings[0]
        for i in range(1, len(meetings)):
            curr_start, curr_end = meetings[i]

            if curr_start <= end:
                end = max(end, curr_end)
            else:
                merged_meetings.append([start, end])
                start, end = curr_start, curr_end

        merged_meetings.append([start, end])

        ans = 0

        ans += max(merged_meetings[0][0] - 1, 0)

        for i in range(1, len(merged_meetings)):
            prev_end = merged_meetings[i - 1][1]
            curr_start = merged_meetings[i][0]
            ans += max(curr_start - prev_end - 1, 0)

        ans += max(days - merged_meetings[-1][1], 0)

        return ans


class TestSolution(unittest.TestCase):
    def test_countDays(self):
        solution = Solution()
        self.assertEqual(solution.countDays(5, [[5, 7], [1, 3], [9, 10]]), 2)


if __name__ == '__main__':
    unittest.main()
