import unittest


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        def binary_search(intervals, newInterval):
            left = 0
            right = len(intervals) - 1
            while left <= right:
                mid = (left + right) // 2

                if intervals[mid][0] == newInterval[0]:
                    return mid

                if intervals[mid][0] < newInterval[0]:
                    left = mid + 1
                else:
                    right = mid - 1

            return right + 1

        idx = binary_search(intervals, newInterval)

        unmerged_intervals = intervals[:idx] + [newInterval] + intervals[idx:]
        n = len(unmerged_intervals)

        prev_start = unmerged_intervals[0][0]
        prev_end = unmerged_intervals[0][1]

        for i in range(1, n):
            curr_start = unmerged_intervals[i][0]
            curr_end = unmerged_intervals[i][1]
            if curr_start <= prev_end:
                new_int = [min(prev_start, curr_start), max(prev_end, curr_end)]
                unmerged_intervals[i] = new_int
                unmerged_intervals[i - 1] = None
                prev_start, prev_end = new_int[0], new_int[1]
                continue
            prev_start, prev_end = curr_start, curr_end

        return [i for i in unmerged_intervals if i is not None]


class TestSolution(unittest.TestCase):
    def test_insert(self):
        solution = Solution()
        self.assertListEqual(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
                             [[1, 2], [3, 10], [12, 16]])


if __name__ == '__main__':
    unittest.main()
