import unittest


class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)

        start_points = sorted([t[0] for t in intervals])
        end_points = sorted([t[1] for t in intervals])

        l = 0
        r = 0

        ans = 0
        count = 0
        while l < n and r < n:
            s = start_points[l]
            e = end_points[r]
            if s <= e:
                l += 1
                count += 1
            else:
                r += 1
                count -= 1
            ans = max(ans, count)

        return ans


class TestSolution(unittest.TestCase):
    def test_minGroups(self):
        solution = Solution()
        self.assertEqual(solution.minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]), 3)


if __name__ == '__main__':
    unittest.main()
